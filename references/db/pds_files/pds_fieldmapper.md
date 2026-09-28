# 字段映射关系-pds_fieldmapper

## 字段映射关系-多语言表 t_pds_fieldmapper_l

- **表名称：** 字段映射关系-多语言表
- **表名：** t_pds_fieldmapper_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_fieldmapper_l_fid |  | fid,flocaleid |
| 2 | pk_pds_fieldmapper_l |  | fpkid |

---

## 字段映射关系-主表 t_pds_fieldmapper

- **表名称：** 字段映射关系-主表
- **表名：** t_pds_fieldmapper

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisv_id | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsourcebill | 来源单据 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | ftargetbill | 目标单据 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 12 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 14 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 15 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_fieldmapper_num |  | fnumber |
| 2 | idx_pds_fieldmapper_sid |  | fsourcebill |
| 3 | idx_pds_fieldmapper_tid |  | ftargetbill |
| 4 | pk_pds_fieldmapper |  | fid |

---

## 字段分录-子表 t_pds_fieldmapperentry

- **表名称：** 字段分录-子表
- **表名：** t_pds_fieldmapperentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcefield | 来源单据字段 | varchar | 50 |  | √ | ' ' | 来源单据字段,枚举: |
| 3 | ftargetfield | 目标单据字段 | varchar | 50 |  | √ | ' ' | 目标单据字段,枚举: |
| 4 | fdefaultvalue | 默认值 | varchar | 50 |  | √ | ' ' | 默认值 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_fieldmapperentry |  | fentryid |
| 2 | idx_pds_fieldmapperentry_fid |  | fid |
