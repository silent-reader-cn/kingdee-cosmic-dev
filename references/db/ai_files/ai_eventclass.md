# 异构数据对接模型-ai_eventclass

## 数据结构-子表 t_ai_eventfields

- **表名称：** 数据结构-子表
- **表名：** t_ai_eventfields

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feventclass | 事件类型 | int8 | 64 |  | √ | 0 | [异构数据对接模型 ai_eventclass](../ai_files/ai_eventclass.md) |
| 3 | fassistant | 辅助资料 | int8 | 64 |  | √ | 0 | [辅助资料分类 bos_assistantdatagroup](../base_files/bos_assistantdatagroup.md) |
| 4 | fdisplayname | fdisplayname | varchar | 100 |  | √ | ' ' |  |
| 5 | fmpformuladesc_tag | 必录条件描述_详情 | text | 0 |  |  | null | 必录条件描述_详情 |
| 6 | ffieldname | 字段编码 | varchar | 50 |  | √ | ' ' | 字段编码 |
| 7 | fismustinput | 必录 | bpchar | 1 |  | √ | ' ' | 必录 |
| 8 | fmustinputformula | 必录条件 | varchar | 1000 |  |  | ' ' | 必录条件 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | frefobj | 基础资料 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 11 | ffieldtype | 字段类型 | varchar | 30 |  | √ | ' ' | 字段类型,枚举: txt :文本 number :数值 date :日期 basedata :基础资料 entry :分录 boolean :布尔 assistant :辅助资料 |
| 12 | fmpformuladesc | 必录条件描述 | varchar | 1000 |  |  | ' ' | 必录条件描述 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_eventfields |  | fid |
| 2 | pk_t_ai_eventfields |  | fentryid |

---

## 数据分录结构-多语言表 t_ai_evententry_l

- **表名称：** 数据分录结构-多语言表
- **表名：** t_ai_evententry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fenfddisplayname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ai_evententry_l |  | fpkid |
| 2 | idx_ai_evententry_l |  | fdetailid,flocaleid |

---

## 数据分录结构-子表 t_ai_evententry

- **表名称：** 数据分录结构-子表
- **表名：** t_ai_evententry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fentryfieldname | 字段编码 | varchar | 50 |  | √ | ' ' | 字段编码 |
| 2 | fentryassistant | 辅助资料 | int8 | 64 |  | √ | 0 | [辅助资料分类 bos_assistantdatagroup](../base_files/bos_assistantdatagroup.md) |
| 3 | fentryrefobj | 基础资料 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 4 | fentryfieldtype | 字段类型 | varchar | 30 |  | √ | ' ' | 字段类型,枚举: txt :文本 number :数值 date :日期 basedata :基础资料 boolean :布尔 entry :分录 assistant :辅助资料 |
| 5 | fentrymformuladesc_tag | 必录条件描述_详情 | text | 0 |  |  | null | 必录条件描述_详情 |
| 6 | fentrymformuladesc | 必录条件描述 | varchar | 1000 |  |  | ' ' | 必录条件描述 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | fentrympformula | 必录条件 | varchar | 1000 |  |  | ' ' | 必录条件 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 11 | fentryismustinput | 必录 | bpchar | 1 |  | √ | ' ' | 必录 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_evententry |  | fentryid |
| 2 | pk_t_ai_evententry |  | fdetailid |

---

## 数据结构-多语言表 t_ai_eventfields_l

- **表名称：** 数据结构-多语言表
- **表名：** t_ai_eventfields_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdisplayname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_eventfields_l |  | fentryid,flocaleid |
| 2 | pk_t_ai_eventfields_l |  | fpkid |

---

## 前置事件-子表 t_ai_preevent

- **表名称：** 前置事件-子表
- **表名：** t_ai_preevent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpreeventclass | 前置事件模型 | int8 | 64 |  | √ | 0 | [异构数据对接模型 ai_eventclass](../ai_files/ai_eventclass.md) |
| 3 | fprestatus | 前置事件状态 | bpchar | 1 |  | √ | ' ' | 前置事件状态,枚举: v :生成凭证 g :产生事件 |
| 4 | fpreevtfield | 前置事件字段 | varchar | 80 |  | √ | ' ' | 前置事件字段 |
| 5 | fevtfield | 关联字段 | varchar | 80 |  | √ | ' ' | 关联字段 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ai_preevent |  | fentryid |
| 2 | idx_ai_preevent |  | fid |

---

## 异构数据对接模型-多语言表 t_ai_eventclass_l

- **表名称：** 异构数据对接模型-多语言表
- **表名：** t_ai_eventclass_l

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
| 1 | pk_t_ai_eventclass_l |  | fpkid |
| 2 | idx_ai_eventclass_l |  | fid,flocaleid |

---

## 异构数据对接模型-主表 t_ai_eventclass

- **表名称：** 异构数据对接模型-主表
- **表名：** t_ai_eventclass

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [异构数据对接模型分组 ai_eventgroup](../ai_files/ai_eventgroup.md) |
| 3 | flatestversion | 是否为最新版本 | bpchar | 1 |  | √ | ' ' | 是否为最新版本 |
| 4 | fenabledtime | fenabledtime | timestamp | 0 |  |  | null |  |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fsourcetype | fsourcetype | varchar | 30 |  | √ | ' ' |  |
| 10 | fdisabledtime | fdisabledtime | timestamp | 0 |  |  | null |  |
| 11 | fdisabledby | fdisabledby | int8 | 64 |  | √ | 0 |  |
| 12 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 13 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fappversion | 是否新模型 | bpchar | 1 |  | √ | '0' | 是否新模型,枚举: 0 :否 1 :是 |
| 16 | frefdatacnt | frefdatacnt | int8 | 64 |  | √ | 0 |  |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fdescription | fdescription | varchar | 50 |  | √ | ' ' |  |
| 19 | fenabledby | fenabledby | int8 | 64 |  | √ | 0 |  |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | ftemplateno | 单据模板 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 22 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 23 | fevtaction | fevtaction | varchar | 30 |  | √ | ' ' |  |
| 24 | fversionnum | 版本编号 | int4 | 32 |  | √ | 1 | 版本编号 |
| 25 | fevtbill | fevtbill | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ai_eventclass |  | fid |
| 2 | idx_ai_eventclass |  | fnumber |
