# 苍穹微服务登记-isc_apic_mservice

## 输入参数分录-子表 t_iscb_mservice_api_in

- **表名称：** 输入参数分录-子表
- **表名：** t_iscb_mservice_api_in

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finput_data_type | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :布尔值 double :浮点数 STRUCT :结构 ENTRIES :列表 ARRAY :数组 Set :集合 |
| 3 | finput_description | 参数描述 | varchar | 250 |  | √ | ' ' | 参数描述 |
| 4 | finput_field | 参数名 | varchar | 150 |  | √ | ' ' | 参数名 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_mservice_api_in |  | fid |
| 2 | pk_t_iscb_mservice_api_in |  | fentryid |

---

## 输出参数分录-子表 t_iscb_mservice_api_out

- **表名称：** 输出参数分录-子表
- **表名：** t_iscb_mservice_api_out

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutput_field | 参数名 | varchar | 150 |  | √ | ' ' | 参数名 |
| 3 | foutput_data_type | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :布尔值 double :浮点数 STRUCT :结构 ENTRIES :列表 ARRAY :数组 Set :集合 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | foutput_description | 参数描述 | varchar | 250 |  | √ | ' ' | 参数描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscb_mservice_api_out |  | fentryid |
| 2 | idx_iscb_mservice_api_out |  | fid |

---

## 苍穹微服务登记-多语言表 t_iscb_mservice_api_l

- **表名称：** 苍穹微服务登记-多语言表
- **表名：** t_iscb_mservice_api_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_mservice_api_l_0 |  | fid,flocaleid |
| 2 | pk_t_iscb_mservice_api_l |  | fpkid |

---

## 苍穹微服务登记-主表 t_iscb_mservice_api

- **表名称：** 苍穹微服务登记-主表
- **表名：** t_iscb_mservice_api

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fservice_type | 微服务类别 | varchar | 60 |  | √ | ' ' | 微服务类别,枚举: bos :平台 biz :业务 isv :二开 |
| 3 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 4 | fmethod | 方法名（method） | varchar | 50 |  | √ | ' ' | 方法名（method） |
| 5 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 6 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 7 | frecord_log | 记录API调用日志 | bpchar | 1 |  | √ | '0' | 记录API调用日志 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fappid | 应用ID（appId） | varchar | 50 |  | √ | ' ' | 应用ID（appId） |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fauth_required | 需要授权 | bpchar | 1 |  | √ | '0' | 需要授权 |
| 12 | fnot_publish | 不发布到开放平台 | bpchar | 1 |  | √ | '0' | 不发布到开放平台 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fnamespace | 命名空间 | varchar | 255 |  | √ | ' ' | 命名空间 |
| 16 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 17 | fwsinputparam | 输入参数名 | varchar | 150 |  | √ | ' ' | 输入参数名 |
| 18 | fin_digest | API参数摘要模板 | varchar | 150 |  | √ | ' ' | API参数摘要模板 |
| 19 | fservice_name | 服务名称（serviceName） | varchar | 100 |  | √ | ' ' | 服务名称（serviceName） |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fcheck_param_type | 校验参数格式 | bpchar | 1 |  | √ | '0' | 校验参数格式 |
| 22 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 23 | fcategory | 分类 | int8 | 64 |  | √ | 0 | [自定义分类 isc_schema_category](../iscb_files/isc_schema_category.md) |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fout_digest | API结果摘要模板 | varchar | 150 |  | √ | ' ' | API结果摘要模板 |
| 26 | fdescription | 服务描述 | varchar | 200 |  | √ | ' ' | 服务描述 |
| 27 | fopenapi_version | 开放平台版本 | varchar | 10 |  | √ | ' ' | 开放平台版本,枚举: 2 :2.0 1 :1.0 |
| 28 | fcloudid | 云ID或工厂类前缀（cloudId） | varchar | 200 |  | √ | ' ' | 云ID或工厂类前缀（cloudId） |
| 29 | fenable | 使用状态 | varchar | 10 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 31 | fdisable_trace | 禁止记录追溯信息 | varchar | 10 |  | √ | ' ' | 禁止记录追溯信息 |
| 32 | fwsoutputparam | 输出参数名 | varchar | 150 |  | √ | ' ' | 输出参数名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscb_mservice_api |  | fid |
| 2 | idx_iscb_mservice_api_n |  | fnumber |
