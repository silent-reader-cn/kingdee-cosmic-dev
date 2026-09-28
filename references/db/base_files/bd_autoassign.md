# 自动分配方案-bd_autoassign

## 自动分配方案-主表 t_bd_autoassign

- **表名称：** 自动分配方案-主表
- **表名：** t_bd_autoassign

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fexecutetime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 6 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 7 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 8 | fctrlstrategy | 分配方式 | varchar | 10 |  | √ | ' ' | 分配方式,枚举: 1 :逐级分配 2 :自由分配 2.1 :分配 2.2 :局部共享 |
| 9 | fappid | 应用标识ID | varchar | 255 |  | √ | ' ' | 应用标识ID |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | xkmaterialautoassign | xkmaterialautoassign | varchar | 255 |  | √ | ' ' |  |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fxkmaterialassign | 物料自动分配项 | varchar | 255 |  | √ | ' ' | 物料自动分配项 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 36 |  | √ | ' ' | 编码 |
| 18 | fentityid | 基础资料标识ID | varchar | 36 |  | √ | ' ' | 基础资料标识ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_autoassign |  | fid |
| 2 | idx_t_bd_autoassign_number |  | fnumber |
| 3 | idx_t_bd_autoassign_fentityid |  | fentityid |

---

## 方案详情分录-子表 t_bd_autoassign_assignorg

- **表名称：** 方案详情分录-子表
- **表名：** t_bd_autoassign_assignorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fisconcludesub | 包含下级 | bpchar | 1 |  | √ | '0' | 包含下级 |
| 4 | fassignorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | forgfilterschemeid | 组织过滤方案 | int8 | 64 |  | √ | 0 | [基础数据组织过滤方案 bd_org_filterscheme](../base_files/bd_org_filterscheme.md) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ffiltercondition | 过滤条件ID | int8 | 64 |  | √ | 0 | 过滤条件ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_autoassign_assignorg |  | fentryid |
| 2 | idx_t_bd_autoassign_asgorg_id |  | fid |

---

## 自动分配方案-多语言表 t_bd_autoassign_l

- **表名称：** 自动分配方案-多语言表
- **表名：** t_bd_autoassign_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_autoassign_l_fid |  | fid,flocaleid |
| 2 | pk_t_bd_autoassign_l |  | fpkid |

---

## 使用组织-多选基础资料表 t_bd_autoassign_useorg

- **表名称：** 使用组织-多选基础资料表
- **表名：** t_bd_autoassign_useorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_autoassign_useorg |  | fpkid |
| 2 | idx_t_bd_autoassign_useorg_id |  | fentryid |
