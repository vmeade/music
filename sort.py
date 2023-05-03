def reverse(self, meta_messages=False):
		#reverseplay
        start_time = time.time()
        input_time = 0.0

        for msg in self:
            input_time += msg.time

            playback_time = time.time() - start_time
            duration_to_next_event = input_time - playback_time

            if duration_to_next_event > 0.0:
                time.sleep(duration_to_next_event)

            if isinstance(msg, MetaMessage) and not meta_messages:
                continue
            else:
                yield msg