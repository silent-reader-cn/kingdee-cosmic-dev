# 接口请求记录-rim_receive_message

## 接口请求记录-主表 t_rim_receive_message

- **表名称：** 接口请求记录-主表
- **表名：** t_rim_receive_message

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fclass | 处理类 | varchar | 30 |  | √ | ' ' | 处理类 |
| 3 | fstate | 状态 | varchar | 4 |  | √ | ' ' | 状态,枚举: 1 :成功 0 :失败 |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fmethod | 处理方法 | varchar | 30 |  | √ | ' ' | 处理方法 |
| 6 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | freq_msg | 请求内容 | varchar | 255 |  | √ | ' ' | 请求内容 |
| 8 | ferror_msg | 错误信息 | varchar | 500 |  | √ | ' ' | 错误信息 |
| 9 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fbizid | 业务id | varchar | 50 |  | √ | ' ' | 业务id |
| 11 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 12 | freq_msg_tag | 请求内容_详情 | text | 0 |  |  | null | 请求内容_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_receive_message |  | fbizid |
| 2 | idx_rim_receive_message_time |  | fcreatetime |
| 3 | pk_rim_receive_message |  | fid |
