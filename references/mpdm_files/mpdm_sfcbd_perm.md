# 车间执行权限-mpdm_sfcbd_perm

## 车间执行权限-主表 t_mpdm_sfcbd_perm

- **表名称：** 车间执行权限-主表
- **表名：** t_mpdm_sfcbd_perm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fdisableuser | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 14 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fname | 姓名 | varchar | 255 |  | √ | ' ' | 姓名 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 用户信息 bos_usergroup_user |
| 19 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 20 | fenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 21 | fenableuser | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 工号 | varchar | 100 |  | √ | ' ' | 工号 |
| 24 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_sfcbd_perm_user |  | fuserid,fcreateorgid |
| 2 | pk_mpdm_sfcbd_perm |  | fid |
| 3 | idx_t_mpdm_sfcbd_perm_createorg |  | fcreateorgid |
| 4 | idx_mpdm_sfcbd_perm_createorg |  | fcreateorgid,forgid |
| 5 | idx_mpdm_sfcbd_perm_useorg |  | fuseorgid |
| 6 | idx_t_mpdm_sfcbd_perm_master |  | fmasterid |

---

## 工作中心权限-多选基础资料表 t_mpdm_sfcbd_perm_wc

- **表名称：** 工作中心权限-多选基础资料表
- **表名：** t_mpdm_sfcbd_perm_wc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 工作中心 sfc_workcenter |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_sfcbd_perm_wc |  | fpkid |
| 2 | idx_mpdm_sfcbd_perm_wc_fidbdid |  | fid,fbasedataid |

---

## 车间权限-多选基础资料表 t_mpdm_sfcbd_perm_wss

- **表名称：** 车间权限-多选基础资料表
- **表名：** t_mpdm_sfcbd_perm_wss

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 车间设置 mpdm_workshopsetup |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_sfcbdperm_wss_fidbdid |  | fid,fbasedataid |
| 2 | pk_mpdm_sfcbd_perm_wss |  | fpkid |

---

## 车间执行权限-使用范围表 t_mpdm_sfcbd_perm_u

- **表名称：** 车间执行权限-使用范围表
- **表名：** t_mpdm_sfcbd_perm_u

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
| 1 | pk_t_mpdm_sfcbd_perm_u |  | fdataid,fuseorgid |
| 2 | idx_t_mpdm_sfcbd_perm_u_uo |  | fuseorgid |

---

## 车间执行权限-多语言表 t_mpdm_sfcbd_perm_l

- **表名称：** 车间执行权限-多语言表
- **表名：** t_mpdm_sfcbd_perm_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 姓名 | varchar | 255 |  | √ | ' ' | 姓名 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_sfcbd_perm_l_fid |  | fid,flocaleid |
| 2 | pk_mpdm_sfcbd_perm_l |  | fpkid |
