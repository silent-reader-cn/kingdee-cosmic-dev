# 工卡断路器信息-mpdm_cbreaker

## 工卡断路器信息-多语言表 t_mpdm_cbreaker_l

- **表名称：** 工卡断路器信息-多语言表
- **表名：** t_mpdm_cbreaker_l

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
| 1 | idx_mpdm_cbreaker_l_0 |  | fid,flocaleid |
| 2 | pk_mpdm_cbreaker_l |  | fpkid |

---

## 工卡断路器信息-使用范围位图表 t_mpdm_cbreaker_m

- **表名称：** 工卡断路器信息-使用范围位图表
- **表名：** t_mpdm_cbreaker_m

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
| 1 | pk_t_mpdm_cbreaker_m |  | forgid |

---

## 工卡断路器信息-使用范围表 t_mpdm_cbreaker_u

- **表名称：** 工卡断路器信息-使用范围表
- **表名：** t_mpdm_cbreaker_u

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
| 1 | idx_t_mpdm_cbreaker_u_uo |  | fuseorgid |
| 2 | pk_t_mpdm_cbreaker_u |  | fdataid,fuseorgid |

---

## 断路器信息-多语言表 t_mpdm_cbentry_l

- **表名称：** 断路器信息-多语言表
- **表名：** t_mpdm_cbentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcbname | 断路器名称 | varchar | 255 |  | √ | ' ' | 断路器名称 |
| 2 | fpanel | 面板 | varchar | 255 |  | √ | ' ' | 面板 |
| 3 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fcbcsystem | 断路器控制系统 | varchar | 255 |  | √ | ' ' | 断路器控制系统 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_cbentry_l |  | fpkid |
| 2 | idx_mpdm_cbentry_l_0 |  | fentryid,flocaleid |

---

## 工卡断路器信息-主表 t_mpdm_cbreaker

- **表名称：** 工卡断路器信息-主表
- **表名：** t_mpdm_cbreaker

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fdisabletime | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fauxproperty | 辅助属性（废弃） | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 14 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fenabler | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fmaterialtype | 检修设备类型 | int8 | 64 |  | √ | 0 | [检修设备类型 mpdm_mrtype](../mpdm_files/mpdm_mrtype.md) |
| 22 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 23 | fenabletime | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 24 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 26 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 27 | fcard | 工卡编码 | int8 | 64 |  | √ | 0 | [工卡 mpdm_mrocardroute](../mpdm_files/mpdm_mrocardroute.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mpdm_cbreaker_createorg |  | fcreateorgid |
| 2 | idx_t_mpdm_cbreaker_corgid |  | fcreateorgid |
| 3 | pk_mpdm_cbreaker |  | fid |
| 4 | idx_t_mpdm_cbreaker_master |  | fmasterid |
| 5 | idx_t_mpdm_cbreaker_fcard |  | fcard |

---

## 断路器信息-子表 t_mpdm_cbentry

- **表名称：** 断路器信息-子表
- **表名：** t_mpdm_cbentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffindmodel | ffindmodel | int8 | 64 |  | √ | 0 |  |
| 3 | fcbname | 断路器名称 | varchar | 255 |  | √ | ' ' | 断路器名称 |
| 4 | fcbposition | 断路器位置 | varchar | 255 |  | √ | ' ' | 断路器位置 |
| 5 | fpanel | 面板 | varchar | 255 |  | √ | ' ' | 面板 |
| 6 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fmrtype | 检修设备类型 | int8 | 64 |  | √ | 0 | [检修设备类型 mpdm_mrtype](../mpdm_files/mpdm_mrtype.md) |
| 10 | fenginemodel | 发动机型号 | int8 | 64 |  | √ | 0 | [发动机型号 mpdm_enginetype](../mpdm_files/mpdm_enginetype.md) |
| 11 | fcbcsystem | 断路器控制系统 | varchar | 255 |  | √ | ' ' | 断路器控制系统 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_cbentry |  | fentryid |
| 2 | idx_mpdm_cbentry_fk |  | fid |
| 3 | idx_t_mpdm_cbentry_fcbname |  | fcbname,fcbposition |
