# 会议内容(废弃)-sfc_meetcontent

## 会议内容(废弃)-使用范围表 t_sfc_meetcontent_u

- **表名称：** 会议内容(废弃)-使用范围表
- **表名：** t_sfc_meetcontent_u

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
| 1 | pk_t_sfc_meetcontent_u |  | fdataid,fuseorgid |
| 2 | idx_t_sfc_meetcontent_u_uo |  | fuseorgid |

---

## 会议内容(废弃)-多语言表 t_sfc_meetcontent_l

- **表名称：** 会议内容(废弃)-多语言表
- **表名：** t_sfc_meetcontent_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_meetcontent_l_0 |  | fid,flocaleid |
| 2 | pk_sfc_meetcontent_l |  | fpkid |

---

## 会议内容(废弃)-主表 t_sfc_meetcontent

- **表名称：** 会议内容(废弃)-主表
- **表名：** t_sfc_meetcontent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmroorderno | 检修工单号 | varchar | 50 |  | √ | ' ' | 检修工单号 |
| 4 | fexpdate | 有效截止日期 | timestamp | 0 |  |  | null | 有效截止日期 |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | frole | 角色 | varchar | 50 |  | √ | ' ' | 角色,枚举: H :行业负责人 J :机主 G :工程师/班组长 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fdepartment | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fnowdate | 当前日期 | timestamp | 0 |  |  | null | 当前日期 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 15 | ftrade | 行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fmratype | 检修设备类型 | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 21 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fmateralregistnum | 检修设备注册号 | int8 | 64 |  | √ | 0 | 物料检修信息 mpdm_materialmtcinfo |
| 23 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 25 | fproject | 项目 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 26 | fcontent | 内容 | varchar | 2000 |  | √ | ' ' | 内容 |
| 27 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_meetcontent_createorg |  | fcreateorgid |
| 2 | pk_sfc_meetcontent |  | fid |
| 3 | idx_t_sfc_meetcontent_master |  | fmasterid |
| 4 | idx_sfc_meetcontent_master |  | fmasterid |
| 5 | idx_t_sfc_meetcontent_createorg |  | fcreateorgid |
| 6 | idx_sfc_meetcontent_number |  | fnumber |

---

## 部门-多选基础资料表 t_sfc_contentmuldept

- **表名称：** 部门-多选基础资料表
- **表名：** t_sfc_contentmuldept

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_contentmuldept |  | fpkid |
| 2 | idx_sfc_contentmuldept_fk |  | fid |
