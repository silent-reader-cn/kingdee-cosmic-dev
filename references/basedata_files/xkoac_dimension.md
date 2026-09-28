# 经营核算维度-xkoac_dimension

## 经营核算维度-主表 t_bas_flex_property

- **表名称：** 经营核算维度-主表
- **表名：** t_bas_flex_property

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 弹性域 | int8 | 64 |  | √ | 0 | 弹性域 bos_flex |
| 2 | ffiltercondition_tag | 大文本_详情 | text | 0 |  |  | null | 大文本_详情 |
| 3 | fseq | fseq | int8 | 64 |  |  | null |  |
| 4 | fdisprops | 显示样式 | varchar | 200 |  | √ | ' ' | 显示样式 |
| 5 | fispreset | fispreset | bpchar | 1 |  | √ | '0' |  |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fassistanttype | 辅助值来源 | int8 | 64 |  |  | null | 辅助资料分类 bos_assistantdatagroup |
| 8 | fdatamaxlen | 值最大长度 | int8 | 64 |  | √ | 20 | 值最大长度 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fvaluesource | 值来源 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fflexfield | 字段名 | varchar | 30 |  | √ | ' ' | 字段名 |
| 14 | fissystem | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 15 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | ffiltercondition | 大文本 | varchar | 512 |  | √ | ' ' | 大文本 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fname | 名称 | varchar | 30 |  | √ | ' ' | 名称 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 21 | findex | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 22 | fvaluetype | 值类型 | bpchar | 1 |  | √ | ' ' | 值类型,枚举: 1 :基础资料 2 :辅助资料 |
| 23 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 24 | forgfunc | 组织职能 | int8 | 64 |  | √ | 0 | 组织职能类型 bos_org_biz |
| 25 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 6 :管控范围内共享 |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 28 | fforbiddate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 31 | fdatatype | 数据类型 | varchar | 200 |  | √ | ' ' | 数据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_flex_property_fid_fnumber_key |  | fid,fnumber |
| 2 | t_bas_flex_property_pkey |  | fentryid |
| 3 | t_bas_flex_property_fflexfield_key |  | fflexfield |
| 4 | idx_bas_flex_prop_fidfnumber |  | fid,fnumber |

---

## 经营核算维度-多语言表 t_bas_flex_property_l

- **表名称：** 经营核算维度-多语言表
- **表名：** t_bas_flex_property_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 60 |  | √ | ' ' | 名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | fdescription | varchar | 200 |  | √ | ' ' |  |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_flex_property_fentryid |  | fentryid,flocaleid |
| 2 | t_bas_flex_property_l_pkey |  | fpkid |
