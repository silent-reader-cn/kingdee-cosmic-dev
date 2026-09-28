# 工作内容类别维护-mpdm_workcategory

## 明细信息-子表 t_mpdm_workdetailinfo

- **表名称：** 明细信息-子表
- **表名：** t_mpdm_workdetailinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称(弃用) | varchar | 50 |  | √ | ' ' | 名称(弃用) |
| 3 | fstatus | 生效状态(弃用) | varchar | 50 |  | √ | ' ' | 生效状态(弃用),枚举: A :生效 B :失效 |
| 4 | fstate | 说明(弃用) | varchar | 255 |  | √ | ' ' | 说明(弃用) |
| 5 | fworkdetailid | 名称 | int8 | 64 |  | √ | 0 | 工作内容明细 mpdm_workscopedetail |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fchecktypeid | 检修级别编码(弃用) | int8 | 64 |  | √ | 0 | 检修级别 mpdm_checktype |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_workdetailinfo |  | fentryid |
| 2 | idx_mpdm_workdetailinfo_fseq |  | fid,fseq |

---

## 工作内容类别维护-主表 t_mpdm_workcategory

- **表名称：** 工作内容类别维护-主表
- **表名：** t_mpdm_workcategory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fname | 类别名称 | varchar | 50 |  | √ | ' ' | 类别名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | faduittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fischecktype | 从检修级别引入(弃用) | bpchar | 1 |  | √ | '0' | 从检修级别引入(弃用) |
| 14 | fstate | 类别说明 | varchar | 255 |  | √ | ' ' | 类别说明 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 20 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 类别编码 | varchar | 30 |  | √ | ' ' | 类别编码 |
| 22 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_workcategory |  | fid |
| 2 | idx_t_mpdm_workcategory_createorg |  | fcreateorgid |
| 3 | idx_mpdm_workcategory_fct |  | fcreatetime |
| 4 | idx_mpdm_workcategory_fcorg |  | fcreateorgid |
| 5 | idx_t_mpdm_workcategory_master |  | fmasterid |
| 6 | idx_mpdm_workcategory_fnum |  | fnumber |

---

## 工作内容类别维护-使用范围位图表 t_mpdm_workcategory_m

- **表名称：** 工作内容类别维护-使用范围位图表
- **表名：** t_mpdm_workcategory_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpdm_workcategory_m |  | forgid |

---

## 工作内容类别维护-多语言表 t_mpdm_workcategory_l

- **表名称：** 工作内容类别维护-多语言表
- **表名：** t_mpdm_workcategory_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 类别名称 | varchar | 50 |  | √ | ' ' | 类别名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_workcategory_l |  | fpkid |
| 2 | idx_mpdm_workcategory_l |  | fid,flocaleid |

---

## 工作内容类别维护-使用范围表 t_mpdm_workcategory_u

- **表名称：** 工作内容类别维护-使用范围表
- **表名：** t_mpdm_workcategory_u

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
| 1 | pk_t_mpdm_workcategory_u |  | fdataid,fuseorgid |
| 2 | idx_t_mpdm_workcategory_u_uo |  | fuseorgid |

---

## 明细信息-多语言表 t_mpdm_workdetailinfo_l

- **表名称：** 明细信息-多语言表
- **表名：** t_mpdm_workdetailinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称(弃用) | varchar | 50 |  | √ | ' ' | 名称(弃用) |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_workdetailinfo_l |  | fpkid |
| 2 | idx_mpdm_workdetailinfo_l |  | fentryid,flocaleid |
