# 本地消息表-bdtaxr_localmessage

## 本地消息表-主表 t_bdtaxr_localmessage

- **表名称：** 本地消息表-主表
- **表名：** t_bdtaxr_localmessage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fattempts | 尝试次数 | int8 | 64 |  | √ | 0 | 尝试次数 |
| 3 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: |
| 4 | ftype | 消息类型 | varchar | 50 |  | √ | ' ' | 消息类型,枚举: |
| 5 | fmessage | 消息内容 | varchar | 255 |  | √ | ' ' | 消息内容 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fqueue | fqueue | varchar | 255 |  | √ | ' ' |  |
| 8 | fsource | 来源 | varchar | 50 |  | √ | ' ' | 来源,枚举: |
| 9 | fmessage_tag | 消息内容_详情 | text | 0 |  |  | null | 消息内容_详情 |
| 10 | fexpiretime | 过期时间 | timestamp | 0 |  |  | null | 过期时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_localmsg_01 |  | fcreatetime |
| 2 | pk_bdtaxr_localmessage |  | fid |
