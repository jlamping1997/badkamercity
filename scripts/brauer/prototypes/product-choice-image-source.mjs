export function firstLinkedProductImage(choice, productsById) {
  if (!choice || choice.linked_product_id == null) return null;
  const product = productsById.get(String(choice.linked_product_id));
  if (!product || product.sku !== choice.sku) return null;
  const image = Array.isArray(product.images) ? product.images[0] : null;
  if (!image || typeof image.src !== 'string' || !image.src.trim()) return null;
  if (image.media_type && image.media_type !== 'image') return null;
  return image;
}

export function replaceLinkedProductImages(productsById, productId, expectedSku, images) {
  const product = productsById.get(String(productId));
  if (!product || product.sku !== expectedSku || !Array.isArray(images)) return false;
  if (!images.every(image => image && typeof image.src === 'string' && (!image.media_type || image.media_type === 'image'))) return false;
  product.images = images.map(image => ({ ...image }));
  return true;
}
