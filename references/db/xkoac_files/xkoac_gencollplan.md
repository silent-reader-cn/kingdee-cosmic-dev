# 生成经营费用归集单方案-xkoac_gencollplan

## 选择经营费用归集方案-子表 t_xkoac_gencollpsub

- **表名称：** 选择经营费用归集方案-子表
- **表名：** t_xkoac_gencollpsub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcollplanid | 归集方案 | int8 | 64 |  | √ | 0 | [经营费用归集方案 xkoac_collplan](../xkoac_files/xkoac_collplan.md) |
| 2 | fplanchecked | 是否选中 | bpchar | 1 |  | √ | '1' | 是否选中 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_gencollpsub |  | fentryid |
| 2 | pk_xkoac_gencollpsub |  | fdetailid |

---

## 选择经营账簿-子表 t_xkoac_gencollpentity

- **表名称：** 选择经营账簿-子表
- **表名：** t_xkoac_gencollpentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fendperiod | 结束期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 3 | forgversion | 经营组织架构版本 | int8 | 64 |  | √ | 0 | [经营组织架构版本 xkoac_orgsystem](../xkoac_files/xkoac_orgsystem.md) |
| 4 | fstartperiod | 开始期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fbookchecked | 是否选中 | bpchar | 1 |  | √ | '1' | 是否选中 |
| 8 | faccountbook | 经营账簿 | int8 | 64 |  | √ | 0 | [经营账簿 xkoac_operatingbook](../xkoac_files/xkoac_operatingbook.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_gcpentity_fid |  | fid |
| 2 | pk_xkoac_gencollpentity |  | fentryid |

---

## 多选经营单元-多选基础资料表 t_xkoac_gencollpunit

- **表名称：** 多选经营单元-多选基础资料表
- **表名：** t_xkoac_gencollpunit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [经营单元 xkoac_unit](../basedata_files/xkoac_unit.md) |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_gencollpunit |  | fpkid |
| 2 | idx_xkoac_gcu_detailid |  | fdetailid |

---

## 生成经营费用归集单方案-多语言表 t_xkoac_gencollplan_l

- **表名称：** 生成经营费用归集单方案-多语言表
- **表名：** t_xkoac_gencollplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_gencollplan_l |  | fid,flocaleid |
| 2 | pk_xkoac_gencollplan_l |  | fpkid |

---

## 生成经营费用归集单方案-主表 t_xkoac_gencollplan

- **表名称：** 生成经营费用归集单方案-主表
- **表名：** t_xkoac_gencollplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_gencollplan |  | fid |
| 2 | idx_xkoac_gcplan_creator |  | fcreatorid |
