# 维度自定义分组-xkbm_dimcustgroup

## 维度自定义分组-多语言表 t_xkbm_dimcustgroup_l

- **表名称：** 维度自定义分组-多语言表
- **表名：** t_xkbm_dimcustgroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
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
| 1 | pk_xkbm_dimcustgroup_l |  | fpkid |
| 2 | idx_t_xkbm_dimcustgroup_l |  | fid,flocaleid |

---

## 自定义分组-子表 t_xkbm_dimgroupentry

- **表名称：** 自定义分组-子表
- **表名：** t_xkbm_dimgroupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimfilterjson | 维度过滤json | varchar | 2000 |  | √ | ' ' | 维度过滤json |
| 3 | ffiltertype | 取值方式 | varchar | 5 |  | √ | ' ' | 取值方式,枚举: 0 :按固定维度取值 1 :按维度过滤取值 |
| 4 | fdimfiltersql | 维度过滤sql | varchar | 2000 |  | √ | ' ' | 维度过滤sql |
| 5 | fcustflexdim | 分组维度弹性域 | int8 | 64 |  | √ | 0 | [主维度组合引用 xkbm_maindimref](../xkbm_files/xkbm_maindimref.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcustdetail | 分组维度 | int8 | 64 |  | √ | 0 | null 010 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_dimgroupentry |  | fentryid |
| 2 | idx_xkbm_dimgroupentry |  | fid |

---

## 维度自定义分组-主表 t_xkbm_dimcustgroup

- **表名称：** 维度自定义分组-主表
- **表名：** t_xkbm_dimcustgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [维度自定义分组分组 xkbm_dimcustgroupgroup](../xkbm_files/xkbm_dimcustgroupgroup.md) |
| 5 | fdetaildimgroup | 对应明细维度 | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fcustomizegroup | 自定义分组维度 | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 8 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 16 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_dimcustgroup |  | fid |
| 2 | idx_xkbm_dimcustgroup |  | fdetaildimgroup |

---

## 对应明细维度-子表 t_xkbm_dimgroupsubentry

- **表名称：** 对应明细维度-子表
- **表名：** t_xkbm_dimgroupsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdetailcreateorg | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | fdimdetail | 明细维度 | int8 | 64 |  | √ | 0 | null 010 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fdetailflexdim | 明细维度弹性域 | int8 | 64 |  | √ | 0 | [主维度组合引用 xkbm_maindimref](../xkbm_files/xkbm_maindimref.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_dimgroupsubentry |  | fdetailid |
| 2 | idx_xkbm_dimgroupsubentry |  | fentryid |
