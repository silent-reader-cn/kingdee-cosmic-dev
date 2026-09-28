# 基础数据管控策略-实体-bd_bdctrlstrtgy

## 基础数据管控策略-实体-多语言表 t_bd_ctrlstrategy_l

- **表名称：** 基础数据管控策略-实体-多语言表
- **表名：** t_bd_ctrlstrategy_l

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
| 1 | idx_ctrlstrategy_l_id |  | fid,flocaleid |
| 2 | t_bd_ctrlstrategy_l_pkey |  | fpkid |

---

## 子单据体-子表 t_bd_ctrlstgyfielddtl

- **表名称：** 子单据体-子表
- **表名：** t_bd_ctrlstgyfielddtl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffieldnumber | 字段编码 | varchar | 100 |  | √ | ' ' | 字段编码 |
| 2 | fisallowupdate | 允许修改 | bpchar | 1 |  | √ | ' ' | 允许修改,枚举: 1 :是 2 :否 |
| 3 | fisfieldlock | fisfieldlock | bpchar | 1 |  | √ | '0' |  |
| 4 | ffielddefaultvalue | 默认值 | varchar | 255 |  | √ | ' ' | 默认值 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | ffieldcontroltype | 控制规则 | varchar | 50 |  | √ | ' ' | 控制规则,枚举: 1 :留空 2 :默认 3 :携带 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fisallowshare | 允许共享 | bpchar | 1 |  | √ | ' ' | 允许共享,枚举: 1 :是 2 :否 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ctrlstgyfielddtl_detail |  | fentryid |
| 2 | t_bd_ctrlstgyfielddtl_pkey |  | fdetailid |

---

## 子单据体-多语言表 t_bd_ctrlstgyfielddtl_l

- **表名称：** 子单据体-多语言表
- **表名：** t_bd_ctrlstgyfielddtl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffieldname | 字段 | varchar | 50 |  | √ | ' ' | 字段 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ctrlstgyfielddtl_l_detail |  | fdetailid,flocaleid |
| 2 | t_bd_ctrlstgyfielddtl_l_pkey |  | fpkid |

---

## 基础数据管控策略-实体-主表 t_bd_ctrlstrategy

- **表名称：** 基础数据管控策略-实体-主表
- **表名：** t_bd_ctrlstrategy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' |  |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fctrlview | fctrlview | int8 | 64 |  | √ | 0 |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fbasedataviewid | 基础数据视图关系 | varchar | 36 |  | √ | ' ' | [基础数据视图关系 bd_basedataview](../base_files/bd_basedataview.md) |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 15 | fcuid | 管控单元 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ctrlstrategy_cu |  | fcuid |
| 2 | t_bd_ctrlstrategy_pkey |  | fid |
| 3 | idx_ctrlstrategy_bdview |  | fbasedataviewid |

---

## 单据体-子表 t_bd_ctrlstrategydetail

- **表名称：** 单据体-子表
- **表名：** t_bd_ctrlstrategydetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fisallowupdate | fisallowupdate | bpchar | 1 |  | √ | ' ' |  |
| 4 | fxkupgradestatus | fxkupgradestatus | bpchar | 1 |  | √ | '0' |  |
| 5 | fxkuseorgid | 使用组织(共享型) | text | 0 |  |  | null | 使用组织(共享型) |
| 6 | fmanagestrategy | 管理策略 | varchar | 10 |  | √ | ' ' | 管理策略,枚举: 1 :管理组织管理 2 :创建组织管理 |
| 7 | fctrltype | 控制类型 | varchar | 10 |  | √ | ' ' | 控制类型,枚举: D :分配 S :共享 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fuseorgid | 使用组织(个性化) | text | 0 |  |  | null | 使用组织(个性化) |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 1 :按管控单元逐级分配 2 :按管控单元自由分配 3 :按组织逐级分配 4 :按组织自由分配 5 :全局共享 6 :管控单位共享 |
| 12 | fisallowshare | fisallowshare | bpchar | 1 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_ctrlstrategydetail_pkey |  | fentryid |
| 2 | idx_ctrlstrategydetail_org |  | fid,fcreateorgid |
