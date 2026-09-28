# 会计事项-ai_bizinfoscheme

## 会计事项-主表 t_ai_bizinfoscheme

- **表名称：** 会计事项-主表
- **表名：** t_ai_bizinfoscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 记账场景描述 | varchar | 200 |  | √ | ' ' | 记账场景描述 |
| 3 | fname | 名称 | varchar | 148 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcondition_tag | 业务分类条件真实字段_详情 | text | 0 |  |  | null | 业务分类条件真实字段_详情 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fbizdate_tag | 业务日期真实字段_详情 | text | 0 |  |  | null | 业务日期真实字段_详情 |
| 8 | fvoucherdate | 记账日期真实字段 | varchar | 255 |  | √ | ' ' | 记账日期真实字段 |
| 9 | fvoucherdate_tag | 记账日期真实字段_详情 | text | 0 |  |  | null | 记账日期真实字段_详情 |
| 10 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreateorg | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | facctorgdesc | 记账组织多语言 | varchar | 255 |  | √ | ' ' | 记账组织多语言 |
| 14 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | facctorgid | 记账组织 | varchar | 50 |  | √ | ' ' | 记账组织,枚举: |
| 18 | fbizdate | 业务日期真实字段 | varchar | 255 |  | √ | ' ' | 业务日期真实字段 |
| 19 | fsourcebillid | 来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fcondition | 业务分类条件真实字段 | varchar | 255 |  | √ | ' ' | 业务分类条件真实字段 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_bizinfoscheme_fsourbill |  | fsourcebillid |
| 2 | pk_ai_bizinfoscheme |  | fid |

---

## 业务信息来源-多语言表 t_ai_bizinfoschemeentry_l

- **表名称：** 业务信息来源-多语言表
- **表名：** t_ai_bizinfoschemeentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsrcbillfieldname | 表达式名称 | varchar | 255 |  | √ | ' ' | 表达式名称 |
| 2 | fsrcbillfielddesc | 业务描述 | varchar | 200 |  | √ | ' ' | 业务描述 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_bizinfoschemeentry_lid |  | fentryid,flocaleid |
| 2 | pk_t_ai_bizinfoschemeentry_l |  | fpkid |

---

## 会计事项-多语言表 t_ai_bizinfoscheme_l

- **表名称：** 会计事项-多语言表
- **表名：** t_ai_bizinfoscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 记账场景描述 | varchar | 200 |  | √ | ' ' | 记账场景描述 |
| 3 | facctorgdesc | 记账组织多语言 | varchar | 255 |  | √ | ' ' | 记账组织多语言 |
| 4 | fname | 名称 | varchar | 148 |  | √ | ' ' | 名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ai_bizinfoscheme_l |  | fpkid |
| 2 | idx_ai_bizinfoscheme_l_lid |  | fid,flocaleid |

---

## 业务信息来源-子表 t_ai_bizinfoschemeentry

- **表名称：** 业务信息来源-子表
- **表名：** t_ai_bizinfoschemeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillfieldname | 表达式名称 | varchar | 255 |  | √ | ' ' | 表达式名称 |
| 3 | flocalamount | 运算表达式 | varchar | 255 |  | √ | ' ' | 运算表达式 |
| 4 | fispresetfield | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 5 | flocalamountdesc | 金额计算 | varchar | 255 |  | √ | ' ' | 金额计算 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentityobjectid | 关联基础资料类型 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | fvaluetype | 取值类型 | bpchar | 1 |  | √ | '0' | 取值类型,枚举: 0 :单个字段 1 :运算表达式 2 :函数表达式 |
| 9 | fisaiinput | 是否传入AI | bpchar | 1 |  | √ | '1' | 是否传入AI |
| 10 | ffieldtype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型 |
| 11 | fsrcbillfielddesc | 业务描述 | varchar | 200 |  | √ | ' ' | 业务描述 |
| 12 | fsrcbillfield | 取值表达式 | varchar | 255 |  | √ | ' ' | 取值表达式 |
| 13 | ffunctionexp | 函数表达式 | varchar | 255 |  | √ | ' ' | 函数表达式 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fassistantdatagroupid | 关联辅助资料类型 | int8 | 64 |  | √ | 0 | [辅助资料分类 bos_assistantdatagroup](../base_files/bos_assistantdatagroup.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ai_bizinfoschemeentry |  | fentryid |
| 2 | idx_ai_bizinfoschemeentry_fk |  | fid |
