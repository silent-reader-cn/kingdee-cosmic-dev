# 辅助资料-bos_assistantdata_detail

## 辅助资料-多语言表 t_bas_assistantdataentry_l

- **表名称：** 辅助资料-多语言表
- **表名：** t_bas_assistantdataentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 2 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_assistantdataentry_l_fentryid_flocaleid_key |  | fentryid,flocaleid |
| 2 | idx_bas_assistantdataentry_l |  | fentryid,flocaleid |
| 3 | t_bas_assistantdataentry_l_pkey |  | fpkid |

---

## 辅助资料-主表 t_bas_assistantdataentry

- **表名称：** 辅助资料-主表
- **表名：** t_bas_assistantdataentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fapproverid | fapproverid | int8 | 64 |  | √ | 0 |  |
| 2 | fgroupid | 类别 | int8 | 64 |  | √ | 0 | 辅助资料分类 bos_assistantdatagroup |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 4 | fforbidstatus | fforbidstatus | bpchar | 1 |  |  | ' ' |  |
| 5 | fseq | 显示顺序 | int8 | 64 |  |  | null | 显示顺序 |
| 6 | fbizappid | fbizappid | varchar | 80 |  | √ | ' ' |  |
| 7 | fstatus | 数据状态 | bpchar | 1 |  |  | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatedate | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmodifydate | 修改时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改时间 |
| 12 | fforbiderid | fforbiderid | int8 | 64 |  | √ | 0 |  |
| 13 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 14 | fapprovedate | fapprovedate | timestamp | 0 |  |  | null |  |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 18 | fparentid | fparentid | bpchar | 36 |  | √ | ' ' |  |
| 19 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 20 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 21 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 22 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | '6' | 控制策略,枚举: 7 :私有 5 :全局共享 |
| 23 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 24 | fparent | 上级辅助资料 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 25 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 27 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 28 | fforbiddate | fforbiddate | timestamp | 0 |  |  | null |  |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_assistantdataentry_pkey |  | fentryid |
| 2 | idx_bas_assistantdataentry_mid |  | fmasterid |
| 3 | idx_bas_assistantdentry_grp |  | fgroupid |
