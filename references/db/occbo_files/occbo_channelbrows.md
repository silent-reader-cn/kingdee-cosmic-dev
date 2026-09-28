# 渠道公告浏览记录-occbo_channelbrows

## 渠道公告浏览记录-主表 t_occbo_chnlannbrows

- **表名称：** 渠道公告浏览记录-主表
- **表名：** t_occbo_chnlannbrows

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 渠道公告主题 | varchar | 255 |  | √ | ' ' | 渠道公告主题 |
| 3 | fcreatorid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 浏览时间 | timestamp | 0 |  |  | null | 浏览时间 |
| 5 | fannounceid | 渠道公告 | int8 | 64 |  | √ | 0 | [渠道公告 occbo_channelannoun](../occbo_files/occbo_channelannoun.md) |
| 6 | fnumber | 渠道公告编号 | varchar | 80 |  | √ | ' ' | 渠道公告编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_chnlannbrows |  | fid |
| 2 | idx_occbo_chnlannbrows_aid |  | fannounceid |
