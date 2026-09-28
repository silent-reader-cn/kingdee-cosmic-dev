# 事件-kem_event

## 事件-多语言表 t_kem_event_l

- **表名称：** 事件-多语言表
- **表名：** t_kem_event_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 事件名称 | varchar | 40 |  | √ | ' ' | 事件名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdesc | 事件描述 | varchar | 1000 |  |  | ' ' | 事件描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_kem_event_l |  | fpkid |
| 2 | idx_kem_event_l_fid |  | fid,flocaleid |

---

## 事件-主表 t_kem_event

- **表名称：** 事件-主表
- **表名：** t_kem_event

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 所属分类 | int8 | 64 |  | √ | 0 | 事件分类 kem_eventgroup |
| 3 | frequestscript | 请求脚本参数 | varchar | 255 |  | √ | ' ' | 请求脚本参数 |
| 4 | fdatasourceid | 数据源 | int8 | 64 |  | √ | 0 | 数据源管理 isc_data_source |
| 5 | fwebapiid | 轮询API | int8 | 64 |  | √ | 0 | WebAPI登记 isc_apic_webapi |
| 6 | fopenapiid | OpenApi | int8 | 64 |  | √ | 0 | API服务 openapi_apilist |
| 7 | fisvid | 开发商标识 | varchar | 20 |  | √ | ' ' | 开发商标识 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 事件状态 | bpchar | 1 |  | √ | ' ' | 事件状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fbiztype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: 1 :选择集成对象 2 :手工输入 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | foperation | 事件 | varchar | 200 |  | √ | ' ' | 事件 |
| 14 | feventuuid | 唯一来源标识 | varchar | 100 |  | √ | ' ' | 唯一来源标识 |
| 15 | feventtype | 事件类型 | bpchar | 1 |  | √ | ' ' | 事件类型,枚举: 2 :Webhook 5 :操作事件 |
| 16 | fname | fname | varchar | 40 |  | √ | ' ' |  |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | frequestconfig | 请求参数 | varchar | 255 |  | √ | ' ' | 请求参数 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | frequestscript_tag | 请求脚本参数_详情 | text | 0 |  |  | null | 请求脚本参数_详情 |
| 21 | fbizobjectid | 业务对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 22 | fbizobjectnumber | 元数据全名 | varchar | 100 |  | √ | ' ' | 元数据全名 |
| 23 | fbizobjectname | 实体单据名称 | varchar | 100 |  | √ | ' ' | 实体单据名称 |
| 24 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 事件编码 | varchar | 120 |  | √ | ' ' | 事件编码 |
| 26 | fdesc | fdesc | varchar | 1000 |  | √ | ' ' |  |
| 27 | frequestconfig_tag | 请求参数_详情 | text | 0 |  |  | null | 请求参数_详情 |
| 28 | feventsourceid | feventsourceid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kem_event_number |  | fnumber |
| 2 | pk_t_kem_event |  | fid |
| 3 | idx_kem_event_dsid |  | fdatasourceid |
| 4 | idx_kem_event_uuid |  | feventuuid |

---

## Data单据体-子表 t_kem_eventpara

- **表名称：** Data单据体-子表
- **表名：** t_kem_eventpara

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisrequired | 必填 | bpchar | 1 |  | √ | ' ' | 必填,枚举: 1 :是 0 :否 |
| 3 | fparadesc | fparadesc | varchar | 255 |  | √ | ' ' |  |
| 4 | fparanumber | fparanumber | varchar | 30 |  | √ | ' ' |  |
| 5 | fparaname | 参数编码 | varchar | 30 |  | √ | ' ' | 参数编码 |
| 6 | fexample | 示例 | varchar | 200 |  | √ | ' ' | 示例 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 9 | fparatype | 参数类型 | varchar | 50 |  | √ | ' ' | 参数类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :布尔值 double :浮点数 ENUM :枚举 STRUCT :结构 mulilang :多语言字符串 unknown :任意值 ENTRIES :分录 REF :基础资料 |
| 10 | fismultivalue | 多值 | bpchar | 1 |  | √ | ' ' | 多值,枚举: 1 :是 0 :否 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fparalevel | 层级 | bpchar | 1 |  | √ | ' ' | 层级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kem_eventpara_fid |  | fid |
| 2 | pk_t_kem_eventpara |  | fentryid |

---

## Data单据体-多语言表 t_kem_eventpara_l

- **表名称：** Data单据体-多语言表
- **表名：** t_kem_eventpara_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fparadesc | 参数说明 | varchar | 255 |  |  | ' ' | 参数说明 |
| 2 | fparanumber | 参数名称 | varchar | 30 |  |  | ' ' | 参数名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  |  | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_kem_eventpara_l |  | fpkid |
| 2 | idx_kem_eventpara_l |  | flocaleid,fentryid |
