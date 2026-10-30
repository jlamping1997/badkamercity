import type { Metadata } from 'next';
import './globals.css';
export const metadata:Metadata={title:'Productcontrole · BadkamerCity',description:'Beoordeel productfoto’s en gegevens per merk. Bewaar je voortgang met checkpoints.',robots:{index:false,follow:false}};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="nl" suppressHydrationWarning><head><script dangerouslySetInnerHTML={{__html:"try{var t=localStorage.getItem('bc-qc-theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');document.documentElement.dataset.theme=t}catch(e){}"}}/></head><body>{children}</body></html>}
