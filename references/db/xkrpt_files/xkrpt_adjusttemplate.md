# 报表调整分录模板-xkrpt_adjusttemplate

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
| 6 | fdatasource | fdatasource | bpchar | 1 |  | √ | '1' |  |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fexplanation | 摘要 | varchar | 2000 |  | √ | ' ' | 摘要 |
| 9 | fitemid | 报表项目编码 | int8 | 64 |  | √ | 0 | [报表项目 xkbd_rptitem](../fibd_files/xkbd_rptitem.md) |
| 10 | fdatatype | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbd_rptitemdatatype](../fibd_files/xkbd_rptitemdatatype.md) |

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

## 模板单据体-子表 t_xkcr_adjustsample_entry

- **表名称：** 模板单据体-子表
- **表名：** t_xkcr_adjustsample_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fsampleid | 报表模板编码 | varchar | 36 |  | √ | ' ' | [报表模板 xkrpt_rptsample](../xkrpt_files/xkrpt_rptsample.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_adjustsample_entry |  | fentryid |
| 2 | idx_xkcr_adjustsample_entry |  | fid |

---

## 报表调整分录模板-多语言表 t_xkcr_adjustentrytemp_l

- **表名称：** 报表调整分录模板-多语言表
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

## 报表调整分录模板-主表 t_xkcr_adjustentrytemp

- **表名称：** 报表调整分录模板-主表
- **表名：** t_xkcr_adjustentrytemp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [调整分录模板分组 xkrpt_adjusttempgroup](../xkrpt_files/xkrpt_adjusttempgroup.md) |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fisspecifyscope | fisspecifyscope | bpchar | 1 |  | √ | '0' |  |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fisallcompany | fisallcompany | bpchar | 1 |  | √ | '0' |  |
| 8 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 9 | fmaintype | 主附表类型 | bpchar | 1 |  | √ | '0' | 主附表类型,枚举: 0 :主表 1 :附表 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fisallsample | 指定范围 | bpchar | 1 |  | √ | '0' | 指定范围 |
| 15 | felimtype | felimtype | int8 | 64 |  | √ | 0 |  |
| 16 | fadjusttype | 调整阶段 | bpchar | 1 |  | √ | ' ' | 调整阶段,枚举: 3 :报表调整 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | fissyspreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 20 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 21 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

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
