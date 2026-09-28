# 辅助属性定义-bd_auxproperty

## 辅助属性定义-主表 t_bas_flex_property

- **表名称：** 辅助属性定义-主表
- **表名：** t_bas_flex_property

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 弹性域 | int8 | 64 |  | √ | 0 | [弹性域 bos_flex](../frame_files/bos_flex.md) |
| 2 | ffiltercondition_tag | 大文本_详情 | text | 0 |  |  | null | 大文本_详情 |
| 3 | fseq | fseq | int8 | 64 |  |  | null |  |
| 4 | fdisprops | 显示样式 | varchar | 200 |  | √ | ' ' | 显示样式 |
| 5 | fispreset | fispreset | bpchar | 1 |  | √ | '0' |  |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fassistanttype | 辅助资料值来源 | int8 | 64 |  |  | null | [辅助资料分类 bos_assistantdatagroup](../base_files/bos_assistantdatagroup.md) |
| 8 | fdatamaxlen | 值最大长度 | int8 | 64 |  | √ | 20 | 值最大长度 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fvaluesource | 基础资料值来源 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fflexfield | 字段名 | varchar | 30 |  | √ | ' ' | 字段名 |
| 14 | fissystem | fissystem | bpchar | 1 |  | √ | '0' |  |
| 15 | fforbidderid | fforbidderid | int8 | 64 |  | √ | 0 |  |
| 16 | ffiltercondition | 大文本 | varchar | 512 |  | √ | ' ' | 大文本 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 21 | findex | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 22 | fvaluetype | 值类型 | bpchar | 1 |  | √ | ' ' | 值类型,枚举: 1 :基础资料 2 :辅助资料 3 :手工输入 |
| 23 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 24 | forgfunc | 组织职能 | int8 | 64 |  | √ | 0 | [组织职能类型 bos_org_biz](../base_files/bos_org_biz.md) |
| 25 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 6 :管控范围内共享 |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 28 | fforbiddate | fforbiddate | timestamp | 0 |  |  | null |  |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
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

## 辅助属性定义-分表 t_bas_flex_property_a

- **表名称：** 辅助属性定义-分表
- **表名：** t_bas_flex_property_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmaxvalue | 最大值 | numeric | 23 | 10 | √ | 0.0000000000 | 最大值 |
| 2 | fminvalue | 最小值 | numeric | 23 | 10 | √ | 0.0000000000 | 最小值 |
| 3 | fistrim | 清除首尾空格 | bpchar | 1 |  | √ | '0' | 清除首尾空格 |
| 4 | fcolwidth | 固定列宽 | int8 | 64 |  | √ | 0 | 固定列宽 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fdatatype | fdatatype | varchar | 5 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_flex_property_a_pkey |  | fentryid |
| 2 | idx_bas_flexpropertyauxpty_a |  | fdatatype |

---

## 辅助属性定义-多语言表 t_bas_flex_property_l

- **表名称：** 辅助属性定义-多语言表
- **表名：** t_bas_flex_property_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
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
