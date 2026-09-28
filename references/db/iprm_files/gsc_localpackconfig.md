# 本地化包-gsc_localpackconfig

## 应用分录-子表 t_gsc_localpackconfigapp

- **表名称：** 应用分录-子表
- **表名：** t_gsc_localpackconfigapp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgscinitappstatus | 初始化状态 | varchar | 2 |  | √ | '0' | 初始化状态,枚举: 0 :未初始化 1 :已初始化 |
| 3 | fgscappstatus | 应用状态 | varchar | 2 |  |  | ' ' | 应用状态,枚举: 1 :禁用 2 :启用 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fgscappname | 应用名称 | varchar | 100 |  | √ | ' ' | 应用名称 |
| 7 | fgscappid | 应用编码 | varchar | 50 |  | √ | ' ' | 应用编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gsc_localpackconfigapp_fid |  | fid |
| 2 | pk_t_gsc_localpackconfigapp |  | fentryid |

---

## 本地化包-多语言表 t_gsc_localpackconfig_l

- **表名称：** 本地化包-多语言表
- **表名：** t_gsc_localpackconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gsc_localpackconfig_l |  | fpkid |
| 2 | idx_gsc_localpackconfig_l_fid |  | fid,flocaleid |

---

## 应用分录-多语言表 t_gsc_localpackconfigapp_l

- **表名称：** 应用分录-多语言表
- **表名：** t_gsc_localpackconfigapp_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fgscappname | 应用名称 | varchar | 100 |  | √ | ' ' | 应用名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gsc_localpackconfigapp_l |  | fpkid |
| 2 | idx_gsc_localpackconfig_l_id |  | fentryid,flocaleid |

---

## 本地化包-主表 t_gsc_localpackconfig

- **表名称：** 本地化包-主表
- **表名：** t_gsc_localpackconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgsccountry | 国家/地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fgscstatus | 启用状态 | varchar | 2 |  | √ | '0' | 启用状态,枚举: 0 :禁用 1 :启用 |
| 11 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gsc_localpackconfig |  | fid |
| 2 | idx_gsc_localpackconfig_land |  | fgsccountry |
| 3 | idx_gsc_localpackconfig_sta |  | fgscstatus |
| 4 | idx_gsc_localpackconfig_num |  | fnumber |

---

## 业务对象分录-多语言表 t_gsc_localpackconfigbus_l

- **表名称：** 业务对象分录-多语言表
- **表名：** t_gsc_localpackconfigbus_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 2 | fgscformname | 表单名称 | varchar | 100 |  | √ | ' ' | 表单名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gsc_localpackconfigbus_l_i |  | fentryid,flocaleid |
| 2 | pk_t_gsc_localpackconfigbus_l |  | fpkid |

---

## 业务对象分录-子表 t_gsc_localpackconfigbus

- **表名称：** 业务对象分录-子表
- **表名：** t_gsc_localpackconfigbus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgscinitbusinessstatus | 初始化状态 | varchar | 2 |  | √ | '0' | 初始化状态,枚举: 0 :未初始化 1 :已初始化 |
| 3 | fgscformname | 表单名称 | varchar | 100 |  | √ | ' ' | 表单名称 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fgscformid | 表单ID | varchar | 50 |  | √ | ' ' | 表单ID |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fgscbusinessstatus | 业务对象状态 | varchar | 2 |  |  | ' ' | 业务对象状态,枚举: 0 :禁用 1 :启用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gsc_localpackconfigbus_fid |  | fid |
| 2 | pk_t_gsc_localpackconfigbus |  | fentryid |
