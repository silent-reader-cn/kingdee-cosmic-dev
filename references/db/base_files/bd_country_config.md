# 国家地区全局设置-bd_country_config

## 国家地区全局设置-主表 t_int_countryconfig

- **表名称：** 国家地区全局设置-主表
- **表名：** t_int_countryconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 开启时间 | timestamp | 0 |  |  | null | 开启时间 |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_int_countryconfig |  | fid |
| 2 | idx_int_cconf_createtime |  | fcreatetime |

---

## 单据体-子表 t_int_countryconfigentry

- **表名称：** 单据体-子表
- **表名：** t_int_countryconfigentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 3 | fregionalformat | 区域格式 | int8 | 64 |  | √ | 0 | 区域格式 inte_programme |
| 4 | flanguage | 语言 | int8 | 64 |  | √ | 0 | 语言种类 inte_language |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | ftimezone | 默认时区 | int8 | 64 |  | √ | 0 | 时区 inte_timezone |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fcountry | 国家地区编码 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_int_countryconfigentry |  | fentryid |
| 2 | idx_t_int_cc_fentry |  | fcountry |
