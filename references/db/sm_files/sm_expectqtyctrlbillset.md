# 可发量控制单据设置-sm_expectqtyctrlbillset

## 可发量控制单据设置-多语言表 t_sm_expectqtyctrlbillset_l

- **表名称：** 可发量控制单据设置-多语言表
- **表名：** t_sm_expectqtyctrlbillset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fsuitorg | 适用组织 | varchar | 500 |  | √ | ' ' | 适用组织 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sm_expectqtyctrlbillset_l |  | fpkid |
| 2 | idx_sm_expectqtyctrlbillset_l |  | fid,flocaleid |

---

## 可发量控制单据设置-主表 t_sm_expectqtyctrlbillset

- **表名称：** 可发量控制单据设置-主表
- **表名：** t_sm_expectqtyctrlbillset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fupanddownbillcheck | 上下游单据同时校验可发量 | bpchar | 1 |  | √ | '0' | 上下游单据同时校验可发量 |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fdescription | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 9 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fneginvstorenotctrl | 允许负库存的仓库不参与可发控制 | bpchar | 1 |  | √ | '0' | 允许负库存的仓库不参与可发控制 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsuitorg | 适用组织 | varchar | 500 |  | √ | ' ' | 适用组织 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 18 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fdoublecheck | 启用双重校验 | bpchar | 1 |  | √ | '0' | 启用双重校验 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_expectqtyctrlbillset |  | fnumber |
| 2 | pk_sm_expectqtyctrlbillset |  | fid |

---

## 控制单据设置-子表 t_sm_ctrlbillsetting

- **表名称：** 控制单据设置-子表
- **表名：** t_sm_ctrlbillsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillformid | 单据名称 | int8 | 64 |  | √ | 0 | [可发量单据配置 sm_expectqtybillsetting](../sm_files/sm_expectqtybillsetting.md) |
| 3 | fctrltimepointid | 控制时点 | int8 | 64 |  | √ | 0 | [可发量操作 sm_expectqtyoperate](../sm_files/sm_expectqtyoperate.md) |
| 4 | fctrlstrength | 控制强度 | bpchar | 1 |  | √ | ' ' | 控制强度,枚举: 0 :禁止 1 :提示 |
| 5 | fctrlrangefilter_tag | 控制范围过滤条件_详情 | text | 0 |  |  | null | 控制范围过滤条件_详情 |
| 6 | fcalrulesld | 可发量计算规则 | int8 | 64 |  | √ | 0 | [可发量计算规则 sm_expectqtycalrules](../sm_files/sm_expectqtycalrules.md) |
| 7 | fctrlrangefilter | 控制范围过滤条件 | varchar | 255 |  | √ | ' ' | 控制范围过滤条件 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fenable | 是否启用校验 | bpchar | 1 |  | √ | '0' | 是否启用校验 |
| 10 | fctrlrangedesc | 控制范围 | varchar | 2000 |  | √ | ' ' | 控制范围 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sm_ctrlbillsetting |  | fentryid |
| 2 | idx_sm_ctrlbillsetting |  | fid |

---

## 适用组织-子表 t_sm_expectqtysuitorg

- **表名称：** 适用组织-子表
- **表名：** t_sm_expectqtysuitorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sm_expectqtysuitorg |  | fentryid |
| 2 | idx_sm_expectqtysuitorg |  | fid |
