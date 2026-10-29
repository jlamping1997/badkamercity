CREATE TABLE `qc_checkpoints` (
	`key` text PRIMARY KEY NOT NULL,
	`owner` text NOT NULL,
	`name` text NOT NULL,
	`payload` text NOT NULL,
	`created` text NOT NULL
);
--> statement-breakpoint
CREATE TABLE `qc_reviews` (
	`key` text PRIMARY KEY NOT NULL,
	`owner` text NOT NULL,
	`item` text NOT NULL,
	`payload` text NOT NULL,
	`revision` integer NOT NULL,
	`action` text NOT NULL,
	`history` text NOT NULL,
	`updated` text NOT NULL
);
