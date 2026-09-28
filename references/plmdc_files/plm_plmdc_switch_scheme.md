# 转换方案-plm_plmdc_switch_scheme

## 转换方案-多语言表 t_plmdc_switch_scheme_l

- **表名称：** 转换方案-多语言表
- **表名：** t_plmdc_switch_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_switch_scheme_l |  | fpkid |
| 2 | idx_plmdc_switch_scheme_l_0 |  | fid,flocaleid |

---

## 转换方案-主表 t_plmdc_switch_scheme

- **表名称：** 转换方案-主表
- **表名：** t_plmdc_switch_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fstart | 启用状态 | bpchar | 1 |  | √ | '0' | 启用状态 |
| 7 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | ftooltype | 转换工具类型 | varchar | 255 |  | √ | ' ' | 转换工具类型,枚举: light :新迪 html :eDrawings |
| 10 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 11 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fswitchtype | 转换类型 | varchar | 30 |  | √ | ' ' | 转换类型,枚举: pdf :PDF light :轻量化 step :STEP转换 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 15 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | floadtype | 浏览服务类型 | varchar | 30 |  | √ | ' ' | 浏览服务类型,枚举: light :新迪 html :eDrawings |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fpreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 20 | fsourcedataid | 原资料id | int4 | 32 |  | √ | 0 | 原资料id |
| 21 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 22 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 24 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_switch_scheme |  | fid |
| 2 | idx_t_plmdc_switch_scheme_createorg |  | fcreateorgid |
| 3 | idx_plmdc_switchscheme_num |  | fnumber |
| 4 | idx_t_plmdc_switch_scheme_master |  | fmasterid |

---

## 转换方案-使用范围表 t_plmdc_switch_scheme_u

- **表名称：** 转换方案-使用范围表
- **表名：** t_plmdc_switch_scheme_u

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
| 1 | idx_t_plmdc_switch_scheme_u_uo |  | fuseorgid |
| 2 | pk_t_plmdc_switch_scheme_u |  | fdataid,fuseorgid |

---

## 转换规则单据体-子表 t_plmdc_switch_rule

- **表名称：** 转换规则单据体-子表
- **表名：** t_plmdc_switch_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdescribe | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fqrcodeid | 二维码方案 | int8 | 64 |  | √ | 0 | 二维码方案 plm_plmdc_qrcodeswitch |
| 4 | fextention | 扩展名（可复选） | varchar | 255 |  | √ | ' ' | 扩展名（可复选）,枚举: |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fendtime | 闲时转换结束时间 | int4 | 32 |  | √ | '-1' | 闲时转换结束时间 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ftool | 转换工具 | varchar | 30 |  | √ | ' ' | 转换工具,枚举: light :新迪 html :eDrawings |
| 9 | fstarttime | 闲时转换开始时间 | int4 | 32 |  | √ | '-1' | 闲时转换开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_switch_rule |  | fentryid |
| 2 | idx_plmdc_switchentry_entry |  | fentryid |
