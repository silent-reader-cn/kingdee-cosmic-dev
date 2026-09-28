# 区域分组-src_region

## 区域分组-主表 t_src_srmregiongroup

- **表名称：** 区域分组-主表
- **表名：** t_src_srmregiongroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 3 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fname | 区域组名称 | varchar | 300 |  | √ | ' ' | 区域组名称 |
| 6 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 1 :逐级分配 2 :自由分配 5 :全局共享 6 :管控范围内共享 7 :私有 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fdepartment | 采购部门 | int8 | 64 |  | √ | 0 | 采购部门 pds_purdepart |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 区域组编码 | varchar | 30 |  | √ | ' ' | 区域组编码 |
| 17 | fpurorg | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_srmregiongroup_number |  | fnumber |
| 2 | pk_src_srmregiongroup |  | fid |

---

## 区域分组-多语言表 t_src_srmregiongroup_l

- **表名称：** 区域分组-多语言表
- **表名：** t_src_srmregiongroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 区域组名称 | varchar | 300 |  | √ | ' ' | 区域组名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_srmregiongroup_l |  | fpkid |
| 2 | idx_src_srmregiongroup_l_fid |  | fid,flocaleid |

---

## 单据体-子表 t_src_srmregionentry

- **表名称：** 单据体-子表
- **表名：** t_src_srmregionentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fenablestatus | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fprovince | 省份 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_srmregionentry |  | fentryid |
| 2 | idx_src_srmregionentry_fid |  | fid |
