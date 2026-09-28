# 税企直连基础信息维护-tsate_baseinfo

## 单据体-子表 t_tsate_base_info_entry

- **表名称：** 单据体-子表
- **表名：** t_tsate_base_info_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fregistrationcode | 系统注册码 | varchar | 50 |  | √ | ' ' | 系统注册码 |
| 3 | faccesstokenurl | 认证地址 | varchar | 50 |  | √ | ' ' | 认证地址 |
| 4 | fauthorizationcode | 系统授权码 | varchar | 50 |  | √ | ' ' | 系统授权码 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fnsrsbh | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fsystemid | 系统编码 | varchar | 50 |  | √ | ' ' | 系统编码 |
| 9 | fbaseurl | 基础地址 | varchar | 50 |  | √ | ' ' | 基础地址 |
| 10 | fenvlable | 环境标识 | varchar | 30 |  | √ | ' ' | 环境标识,枚举: 0 :测试环境 1 :正式环境 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tsate_base_info_entry |  | fentryid |
| 2 | idx_tsate_base_info_entry |  | fid |

---

## 税企直连基础信息维护-主表 t_tsate_base_info

- **表名称：** 税企直连基础信息维护-主表
- **表名：** t_tsate_base_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsupplier | 供应商 | varchar | 30 |  | √ | ' ' | 供应商,枚举: 0 :ASBC 1 :CloudCC |
| 3 | fenvlable | 环境标识 | varchar | 50 |  | √ | ' ' | 环境标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_base_info |  | fenvlable,fsupplier |
| 2 | pk_tsate_base_info |  | fid |
