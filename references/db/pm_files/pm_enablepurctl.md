# 可采控制单据配置-pm_enablepurctl

## 单据类型-多选基础资料表 t_pm_enablepurcfg_type

- **表名称：** 单据类型-多选基础资料表
- **表名：** t_pm_enablepurcfg_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_enablepurcfg_type_fk |  | fid |
| 2 | pk_t_pm_enablepurcfg_type |  | fpkid |

---

## 适用组织-多选基础资料表 t_pm_enablepurcfg_useorg

- **表名称：** 适用组织-多选基础资料表
- **表名：** t_pm_enablepurcfg_useorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pm_enablepurcfg_useorg |  | fpkid |
| 2 | idx_pm_enablepurcfg_useorg_fk |  | fid |

---

## 可采控制单据配置-主表 t_pm_enablepurcfg

- **表名称：** 可采控制单据配置-主表
- **表名：** t_pm_enablepurcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillformid | 单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fcontrolfilter | 控制范围过滤条件 | varchar | 255 |  | √ | ' ' | 控制范围过滤条件 |
| 9 | fcontrolfilter_tag | 控制范围过滤条件_详情 | text | 0 |  |  | null | 控制范围过滤条件_详情 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcontrolfrom | 控制来源 | varchar | 50 |  | √ | ' ' | 控制来源,枚举: A :货源清单 B :采购价目表 C :物料采购信息.采购员 D :物料采购信息.采购组 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fcontrolintensity | 控制强度 | varchar | 50 |  | √ | ' ' | 控制强度,枚举: A :强控制 B :弱控制 |
| 17 | fcontrolscope | 控制范围 | varchar | 2000 |  | √ | ' ' | 控制范围 |
| 18 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fbillentity | 单据名称 | varchar | 50 |  | √ | ' ' | 单据名称,枚举: pm_purorderbill :采购订单 pm_purapplybill :采购申请单 conm_purcontract :采购合同 |
| 21 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pm_enablepurcfg |  | fid |
| 2 | idx_pm_enablepurcfg_m0 |  | fmasterid |

---

## 可采控制单据配置-多语言表 t_pm_enablepurcfg_l

- **表名称：** 可采控制单据配置-多语言表
- **表名：** t_pm_enablepurcfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pm_enablepurcfg_l |  | fpkid |
| 2 | idx_pm_enablepurcfg_l_0 |  | fid,flocaleid |
