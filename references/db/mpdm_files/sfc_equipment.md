# 设备-sfc_equipment

## 设备-多语言表 t_sfc_equipment_l

- **表名称：** 设备-多语言表
- **表名：** t_sfc_equipment_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 设备名称 | varchar | 255 |  | √ | ' ' | 设备名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | '' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  |  | null | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sfc_equipment_l |  | fpkid |

---

## 设备-使用范围表 t_sfc_equipment_u

- **表名称：** 设备-使用范围表
- **表名：** t_sfc_equipment_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sfc_equipment_u |  | fdataid,fuseorgid |
| 2 | idx_t_sfc_equipment_u_uo |  | fuseorgid |

---

## 设备-主表 t_sfc_equipment

- **表名称：** 设备-主表
- **表名：** t_sfc_equipment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 设备类型 | int8 | 64 |  |  | null | 设备类型 sfc_equipgroup |
| 3 | forgid | 组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fsource | 来源 | bpchar | 1 |  | √ | '0' | 来源,枚举: 0 :手工添加 1 :接口同步 |
| 6 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdepartid | 使用部门 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 9 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 13 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  |  | null | 原资料id |
| 15 | fbitindex | 位图 | int8 | 64 |  |  | null | 位图 |
| 16 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 18 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 19 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fequipstatus | 设备状态 | bpchar | 1 |  | √ | 'A' | 设备状态,枚举: A :使用 B :维修 C :故障 D :报废 |
| 22 | fdescription | 描述 | varchar | 255 |  |  | null | 描述 |
| 23 | fenabler | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '5' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | fenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | ftypes | 设备类型 | varchar | 80 |  |  | null | 设备类型 |
| 28 | fnumber | 设备编码 | varchar | 80 |  | √ | ' ' | 设备编码 |
| 29 | fuseorgid | 业务组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 30 | fsourcebitindex | 原资料位图 | int8 | 64 |  |  | null | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_sfc_equipment_createorg |  | fcreateorgid |
| 2 | pk_t_sfc_equipment |  | fid |
| 3 | idx_t_sfc_equipment_master |  | fmasterid |
