# 手机号码格式-cts_telephoneformat

## 单据体-子表 t_cts_telephoneformat

- **表名称：** 单据体-子表
- **表名：** t_cts_telephoneformat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fdigit | 位数 | varchar | 64 |  | √ | ' ' | 位数 |
| 5 | fseq | 分录行号 | int2 | 16 |  | √ | 0 | 分录行号 |
| 6 | fcountryid | 国家或地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fsegment | 起始号段 | varchar | 1024 |  | √ | ' ' | 起始号段 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fissystem | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 11 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fischeck | 启用校验 | bpchar | 1 |  | √ | '0' | 启用校验,枚举: 0 :否 1 :是 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cts_telformat_country |  | fcountryid |
| 2 | pk_cts_telephoneformat |  | fentryid |

---

## 手机号码格式-主表 t_cts_telephone

- **表名称：** 手机号码格式-主表
- **表名：** t_cts_telephone

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | fstatus | varchar | 10 |  | √ | ' ' |  |
| 3 | fmodifierid | 单据修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 单据创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 单据创建时间 | timestamp | 0 |  |  | null | 单据创建时间 |
| 6 | fmodifytime | 单据修改时间 | timestamp | 0 |  |  | null | 单据修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cts_telephone |  | fid |
| 2 | idx_cts_telephone |  | fstatus |
