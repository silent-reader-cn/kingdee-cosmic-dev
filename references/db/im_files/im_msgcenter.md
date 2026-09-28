# 消息中心-im_msgcenter

## 消息中心-主表 t_im_msgcenter

- **表名称：** 消息中心-主表
- **表名：** t_im_msgcenter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freceiveusers | 接受人 | varchar | 500 |  |  | ' ' | 接受人 |
| 3 | fbizdataid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 4 | fentitynumber | 业务对象 | varchar | 50 |  | √ | ' ' | 业务对象 |
| 5 | freadstate | 阅读状态 | varchar | 5 |  | √ | ' ' | 阅读状态,枚举: 0 :未读 1 :已读 |
| 6 | ftitle | 标题 | varchar | 100 |  | √ | ' ' | 标题 |
| 7 | ftype | 消息类型 | varchar | 5 |  | √ | ' ' | 消息类型,枚举: 0 :页面处理 1 :url处理 |
| 8 | fsenduser | 发送人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | freadtime | 阅读时间 | timestamp | 0 |  |  | null | 阅读时间 |
| 10 | fsendtime | 发送日期 | timestamp | 0 |  |  | null | 发送日期 |
| 11 | fcontenturl | 详细信息URL | varchar | 300 |  |  | ' ' | 详细信息URL |
| 12 | fcontent | 正文 | text | 0 |  |  | null | 正文 |
| 13 | foperation | 操作 | varchar | 50 |  | √ | ' ' | 操作 |
| 14 | ftagmap | 自定义标签组 | varchar | 300 |  |  | ' ' | 自定义标签组 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_msgcenter_title |  | ftitle |
| 2 | t_im_msgcenter_pkey |  | fid |
