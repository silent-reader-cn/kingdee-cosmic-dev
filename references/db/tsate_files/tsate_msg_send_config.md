# 消息发送配置-tsate_msg_send_config

## 消息发送配置-主表 t_tsate_msgconfig

- **表名称：** 消息发送配置-主表
- **表名：** t_tsate_msgconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fnodetype | 系统类型 | varchar | 30 |  | √ | ' ' | 系统类型,枚举: |
| 4 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 5 | fmsgurl | URL | varchar | 600 |  | √ | ' ' | URL |
| 6 | fsendtype | 发送类型 | varchar | 30 |  | √ | ' ' | 发送类型,枚举: post :post get :get |
| 7 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | fmsgtype | 消息类型 | varchar | 30 |  | √ | ' ' | 消息类型,枚举: |
| 9 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_msgconfig |  | fnodetype,fmsgtype,fmsgurl,fsendtype |
| 2 | pk_tsate_msgconfig |  | fid |

---

## 单据体-子表 t_tsate_msgconfig_detail

- **表名称：** 单据体-子表
- **表名：** t_tsate_msgconfig_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparavalue | 参数值 | varchar | 100 |  | √ | ' ' | 参数值 |
| 3 | fparaname | 参数名 | varchar | 100 |  | √ | ' ' | 参数名 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tsate_msgconfig_detail |  | fentryid |
| 2 | idx_tsate_msgconfig_detail_fk |  | fid |
