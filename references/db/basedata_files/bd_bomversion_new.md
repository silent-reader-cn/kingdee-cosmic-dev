# 物料版本-bd_bomversion_new

## 物料版本-多语言表 t_bd_materialversion_l

- **表名称：** 物料版本-多语言表
- **表名：** t_bd_materialversion_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 3 | fname | 物料版本名称 | varchar | 50 |  | √ | ' ' | 物料版本名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_materialversion_l |  | fid,flocaleid |
| 2 | pk_bd_materialversion_l |  | fpkid |

---

## 单据体-子表 t_bd_materialversionentry

- **表名称：** 单据体-子表
- **表名：** t_bd_materialversionentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 3 | frelationtype | 关联方式 | varchar | 50 |  | √ | ' ' | 关联方式,枚举: S :手工关联 Z :自动关联 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_materialversionentry |  | fid |
| 2 | pk_bd_materialversionentry |  | fentryid |

---

## 物料版本-主表 t_bd_materialversion

- **表名称：** 物料版本-主表
- **表名：** t_bd_materialversion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 4 | fname | 物料版本名称 | varchar | 50 |  | √ | ' ' | 物料版本名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | finvaliddate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 7 | fenableorid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 10 | feffectdate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 13 | fenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 14 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 物料版本编码 | varchar | 100 |  | √ | ' ' | 物料版本编码 |
| 19 | fversion | PLM版本 | varchar | 50 |  | √ | ' ' | PLM版本,枚举: |
| 20 | fdisableorid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_materialversion |  | fid |
| 2 | idx_bd_materialversion |  | fmaterialid,fversion |
