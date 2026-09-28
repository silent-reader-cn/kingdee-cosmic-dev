# 打印方案-bos_printingscheme

## 打印方案-多语言表 t_bas_printingscheme_l

- **表名称：** 打印方案-多语言表
- **表名：** t_bas_printingscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_printingscheme_l_pkey |  | fpkid |
| 2 | idx_bas_printingscheme_l |  | fid,flocaleid |

---

## 单据体-子表 t_bas_printingcondition

- **表名称：** 单据体-子表
- **表名：** t_bas_printingcondition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffiltername | 过滤条件 | varchar | 100 |  |  | ' ' | 过滤条件 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | ffiltertemplateid | 打印模板 | varchar | 36 |  |  | ' ' | 打印模板,枚举: |
| 4 | ffiltertype | 类型 | varchar | 36 |  |  | ' ' | 类型,枚举: 1 :匹配 2 :其它 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ffiltercondition | 条件 | text | 0 |  |  | null | 条件 |
| 8 | fischeck | 启用 | bpchar | 1 |  |  | '1' | 启用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_printingcondition |  | fid |
| 2 | t_bas_printingcondition_pkey |  | fentryid |

---

## 打印方案-主表 t_bas_printingscheme

- **表名称：** 打印方案-主表
- **表名：** t_bas_printingscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapprovedate | fapprovedate | timestamp | 0 |  |  | null |  |
| 3 | fapproverid | fapproverid | int8 | 64 |  | √ | 0 |  |
| 4 | fbillformid | 业务实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fispreference | 首选方案 | bpchar | 1 |  | √ | '0' | 首选方案 |
| 6 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fdefaulttemplate | 默认模板 | varchar | 36 |  |  | ' ' | 默认模板,枚举: |
| 8 | fapproveline | 审批线路 | varchar | 36 |  | √ | ' ' | 审批线路,枚举: all :所有审批记录 allConsent :所有审批同意记录 lastedConsent :当前节点之前最新审批同意记录 |
| 9 | fdefaultcloudprinter | 默认打印机 | int8 | 64 |  | √ | 0 | [云打印机 bos_cloudprinter](../frame_files/bos_cloudprinter.md) |
| 10 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 11 | fforbidstatus | fforbidstatus | bpchar | 1 |  | √ | ' ' |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改时间 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fsingleactivity | 审批节点 | varchar | 36 |  | √ | ' ' | 审批节点,枚举: all :所有审批记录 allConsent :所有审批同意记录 lastedConsent :当前节点之前最新审批同意记录 |
| 15 | fincludesubmit | 打印时包含人工节点 | bpchar | 1 |  | √ | ' ' | 打印时包含人工节点 |
| 16 | fincludeimage | 打印时包含影像上传节点 | bpchar | 1 |  | √ | ' ' | 打印时包含影像上传节点 |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fforbiderid | fforbiderid | int8 | 64 |  | √ | 0 |  |
| 20 | fordertype | 审批线路排序方式 | varchar | 255 |  | √ | ' ' | 审批线路排序方式,枚举: default :空 asc :顺序 desc :倒序 |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fdefaultprinter | 打印机 | varchar | 36 |  |  | ' ' | 打印机,枚举: |
| 23 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 24 | fforbiddate | fforbiddate | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_printingscheme_pkey |  | fid |
| 2 | idx_bas_printingscheme |  | fnumber |
