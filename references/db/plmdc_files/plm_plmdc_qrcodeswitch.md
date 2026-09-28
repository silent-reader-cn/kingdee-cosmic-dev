# 二维码方案-plm_plmdc_qrcodeswitch

## 二维码方案-多语言表 t_plmdc_qrcodeswitch_l

- **表名称：** 二维码方案-多语言表
- **表名：** t_plmdc_qrcodeswitch_l

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
| 1 | pk_t_plmdc_qrcodeswitch_l |  | fpkid |
| 2 | idx_plmdc_qrcodeswitch_l_0 |  | fid,flocaleid |

---

## 二维码信息配置-子表 t_plmdc_qrcode_entry

- **表名称：** 二维码信息配置-子表
- **表名：** t_plmdc_qrcode_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flabelapnum | 编码段 | varchar | 30 |  | √ | ' ' | 编码段 |
| 3 | faddstyle | 补位 | varchar | 8 |  | √ | ' ' | 补位,枚举: right :右侧 left :左侧 |
| 4 | flength | 长度 | int4 | 32 |  | √ | 0 | 长度 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fattusingmode | 使用模式 | varchar | 16 |  | √ | ' ' | 使用模式,枚举: A :完全取值 B :属性截断 |
| 7 | faddchar | 补位符号 | varchar | 8 |  | √ | ' ' | 补位符号 |
| 8 | ffixval | 设置值 | varchar | 255 |  | √ | ' ' | 设置值 |
| 9 | fsplitsignentry | 段间分隔符 | varchar | 16 |  | √ | ' ' | 段间分隔符,枚举: * :* - :- empty :空 |
| 10 | fcutstyle | 截去 | varchar | 8 |  | √ | ' ' | 截去,枚举: right :右侧 left :左侧 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fattributetype | 属性类型 | varchar | 8 |  | √ | ' ' | 属性类型,枚举: 1 :常量 8 :业务对象字段 |
| 13 | fvalueatributeshow | 编码来源 | varchar | 80 |  | √ | ' ' | 编码来源 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_qrcode_entry |  | fentryid |
| 2 | pk_t_plmdc_qrcode_entry |  | fentryid |

---

## 二维码方案-使用范围表 t_plmdc_qrcodeswitch_u

- **表名称：** 二维码方案-使用范围表
- **表名：** t_plmdc_qrcodeswitch_u

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
| 1 | pk_t_plmdc_qrcodeswitch_u |  | fdataid,fuseorgid |
| 2 | idx_t_plmdc_qrcodeswitch_u_uo |  | fuseorgid |

---

## 二维码方案-主表 t_plmdc_qrcodeswitch

- **表名称：** 二维码方案-主表
- **表名：** t_plmdc_qrcodeswitch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fpreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 10 | fsourcedataid | 原资料id | int4 | 32 |  | √ | 0 | 原资料id |
| 11 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 12 | fexample | 文本示例 | varchar | 255 |  | √ | ' ' | 文本示例 |
| 13 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fstart | 启用状态 | bpchar | 1 |  | √ | '0' | 启用状态 |
| 18 | fleftmargin | 左边距 | int4 | 32 |  | √ | 0 | 左边距 |
| 19 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 20 | fmarginbottom | 下边距 | int4 | 32 |  | √ | 0 | 下边距 |
| 21 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fbizobjectid | 业务模型 | int8 | 64 |  | √ | 0 | [PDM模型 plm_plmsm_modeltreedata](../plmsm_files/plm_plmsm_modeltreedata.md) |
| 23 | fsize | 二维码大小（PX） | int4 | 32 |  | √ | 0 | 二维码大小（PX） |
| 24 | fqrcodetype | 二维码类型 | varchar | 50 |  | √ | ' ' | 二维码类型,枚举: txt :文本二维码 |
| 25 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 27 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 28 | fdimension | 调整维度 | varchar | 30 |  | √ | ' ' | 调整维度,枚举: ratio :比例（%） size :尺寸（PX） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plmdc_qrcodeswitch_createorg |  | fcreateorgid |
| 2 | idx_t_plmdc_qrcodeswitch_master |  | fmasterid |
| 3 | pk_t_plmdc_qrcodeswitch |  | fid |
| 4 | idx_plmdc_qrcodeswitch_num |  | fnumber |
