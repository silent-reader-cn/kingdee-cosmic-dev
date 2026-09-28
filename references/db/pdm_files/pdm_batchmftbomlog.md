# BOM批量修改日志-pdm_batchmftbomlog

## BOM批量修改日志-多语言表 t_pdm_mftbomlog_l

- **表名称：** BOM批量修改日志-多语言表
- **表名：** t_pdm_mftbomlog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pdm_mftbomlog_l |  | fpkid |
| 2 | idx_pdm_mftbomlog_l |  | fid,flocaleid |

---

## BOM批量修改日志-使用范围位图表 t_pdm_mftbomlog_m

- **表名称：** BOM批量修改日志-使用范围位图表
- **表名：** t_pdm_mftbomlog_m

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
| 1 | pk_t_pdm_mftbomlog_m |  | forgid |

---

## BOM批量修改日志-主表 t_pdm_mftbomlog

- **表名称：** BOM批量修改日志-主表
- **表名：** t_pdm_mftbomlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgchange | 变更组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fupdatetype | 变更方式 | varchar | 8 |  | √ | ' ' | 变更方式,枚举: A :直接变更 B :ECN变更 |
| 6 | fcreatetime | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fsavecontent | 变更字段内容 | text | 0 |  |  | null | 变更字段内容 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '5' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | ftype | 变更类型 | bpchar | 1 |  | √ | ' ' | 变更类型,枚举: A :新增子项 B :修改子项 C :替换子项 D :失效子项 E :删除子项 |
| 16 | fcontent_tag | 修改内容-大文本_详情 | text | 0 |  |  | null | 修改内容-大文本_详情 |
| 17 | fsavecontent_tag | 变更字段内容_详情 | text | 0 |  |  | null | 变更字段内容_详情 |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 64 |  | √ | ' ' | 编码 |
| 22 | fcontent | 修改内容-大文本 | text | 0 |  |  | null | 修改内容-大文本 |
| 23 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 24 | fshowcontent | 修改内容 | varchar | 64 |  | √ | ' ' | 修改内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_mftbomlog_modify |  | fmodifytime,fmodifierid |
| 2 | idx_t_pdm_mftbomlog_master |  | fmasterid |
| 3 | pk_t_pdm_mftbomlog |  | fid |
| 4 | idx_t_pdm_mftbomlog_createorg |  | fcreateorgid |

---

## BOM批量修改日志-使用范围表 t_pdm_mftbomlog_u

- **表名称：** BOM批量修改日志-使用范围表
- **表名：** t_pdm_mftbomlog_u

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
| 1 | idx_t_pdm_mftbomlog_u_uo |  | fuseorgid |
| 2 | pk_t_pdm_mftbomlog_u |  | fdataid,fuseorgid |

---

## 日志详情-子表 t_pdm_mftbomlogdetail

- **表名称：** 日志详情-子表
- **表名：** t_pdm_mftbomlogdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbommaterialid | 产品编码ID | int8 | 64 |  | √ | 0 | 产品编码ID |
| 3 | fbomid | BOM内码 | int8 | 64 |  | √ | 0 | BOM内码 |
| 4 | fbomauxpropertyid | 辅助属性ID | int8 | 64 |  | √ | 0 | 辅助属性ID |
| 5 | fbommaterialnumber | 产品编码 | varchar | 80 |  | √ | ' ' | 产品编码 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fexeresult | 执行结果 | varchar | 1024 |  |  | ' ' | 执行结果 |
| 8 | fbomnumber | BOM编码 | varchar | 60 |  | √ | ' ' | BOM编码 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fchangestatus | 执行状态 | bpchar | 1 |  | √ | ' ' | 执行状态,枚举: A :成功 B :失败 |
| 11 | fbommaterialname | fbommaterialname | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pdm_mftbomlogdetail |  | fentryid |
| 2 | idx_pdm_bomlogdetail_compose |  | fid,fbomid |

---

## 日志详情-多语言表 t_pdm_mftbomlogdetail_l

- **表名称：** 日志详情-多语言表
- **表名：** t_pdm_mftbomlogdetail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fbommaterialname | 产品名称 | varchar | 255 |  | √ | ' ' | 产品名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_mftbomlogdetail_l |  | fentryid |
| 2 | pk_t_pdm_mftbomlogdetail_l |  | fpkid |
