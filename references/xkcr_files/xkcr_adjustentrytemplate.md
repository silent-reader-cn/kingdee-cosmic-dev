# 调整分录模板-xkcr_adjustentrytemplate

## 分录明细单据体-子表 t_xkcr_adjusttempentity

- **表名称：** 分录明细单据体-子表
- **表名：** t_xkcr_adjusttempentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fismulesp | 股权分段计算 | bpchar | 1 |  | √ | '0' | 股权分段计算 |
| 3 | fdc | 借贷方向 | bpchar | 1 |  | √ | '1' | 借贷方向,枚举: 1 :借方 2 :贷方 3 :条件判断 |
| 4 | fformula | 调整数 | varchar | 2000 |  | √ | ' ' | 调整数 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdatasource | 取数方 | bpchar | 1 |  | √ | '1' | 取数方,枚举: 1 :本组织 2 :被投资方 3 :借贷差额 4 :投资方 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fexplanation | 摘要 | varchar | 2000 |  | √ | ' ' | 摘要 |
| 9 | fitemid | 报表项目编码 | int8 | 64 |  | √ | 0 | 报表项目 xkbd_rptitem |
| 10 | fdatatype | 项目数据类型 | int8 | 64 |  | √ | 0 | 项目数据类型 xkbd_rptitemdatatype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_adjusttempentity |  | fentryid |
| 2 | idx_xkcr_adjtmpentry |  | fid |

---

## 调整分录模板-主表 t_xkcr_adjustentrytemp

- **表名称：** 调整分录模板-主表
- **表名：** t_xkcr_adjustentrytemp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 模板分组 xkcr_adjusttempgroup |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fisspecifyscope | 指定范围 | bpchar | 1 |  | √ | '0' | 指定范围 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fisallcompany | fisallcompany | bpchar | 1 |  | √ | '0' |  |
| 8 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | felimtype | 调整类型 | int8 | 64 |  | √ | 0 | 抵销类型 xkcr_eliminationtype |
| 14 | fadjusttype | 调整阶段 | bpchar | 1 |  | √ | ' ' | 调整阶段,枚举: 1 :集团调整 2 :报前调整 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 17 | fissyspreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 18 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 19 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_adjtmpentry1 |  | fnumber |
| 2 | idx_xkcr_adjtmpentry2 |  | fgroupid |
| 3 | pk_xkcr_adjustentrytemp |  | fid |
| 4 | idx_xkcr_adjtentry_elim |  | felimtype |

---

## 使用公司单据体-子表 t_xkcr_companyentry

- **表名称：** 使用公司单据体-子表
- **表名：** t_xkcr_companyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomtype | 公司类型 | varchar | 20 |  | √ | ' ' | 公司类型,枚举: bos_org :核算组织 |
| 3 | fcompany | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_companyentry |  | fentryid |
| 2 | idx_xkcr__adjcomentry1 |  | fid |

---

## 调整分录模板-多语言表 t_xkcr_adjustentrytemp_l

- **表名称：** 调整分录模板-多语言表
- **表名：** t_xkcr_adjustentrytemp_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_adjustentrytemp_l |  | fpkid |
| 2 | idx_xkcr_adjustentrytemp_l |  | fid,flocaleid |

---

## 分录明细单据体-多语言表 t_xkcr_adjusttempentity_l

- **表名称：** 分录明细单据体-多语言表
- **表名：** t_xkcr_adjusttempentity_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fexplanation | 摘要 | varchar | 2000 |  | √ | ' ' | 摘要 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_adjtmpent_l1 |  | fentryid,flocaleid |
| 2 | pk_xkcr_adjusttempentity_l |  | fpkid |
