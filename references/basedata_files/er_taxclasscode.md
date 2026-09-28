# 税收分类编码-er_taxclasscode

## 税收分类编码-主表 t_er_taxclasscode

- **表名称：** 税收分类编码-主表
- **表名：** t_er_taxclasscode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fofficecode | 统计局编码 | varchar | 1000 |  | √ | ' ' | 统计局编码 |
| 3 | fishidden | 是否隐藏 | bpchar | 1 |  | √ | ' ' | 是否隐藏 |
| 4 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 5 | fexcisemanagement | 消费税管理 | varchar | 100 |  | √ | ' ' | 消费税管理 |
| 6 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 7 | fsumitem | 汇总项 | bpchar | 1 |  | √ | ' ' | 汇总项 |
| 8 | fvatspecialnum | 增值税特殊代码 | varchar | 80 |  | √ | ' ' | 增值税特殊代码 |
| 9 | fsource | 来源类型 | bpchar | 1 |  | √ | ' ' | 来源类型,枚举: 1 :Excel导入 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fkey | 关键字 | varchar | 2000 |  | √ | ' ' | 关键字 |
| 15 | fversion | 版本号 | varchar | 100 |  | √ | ' ' | 版本号 |
| 16 | fparentnum | 上级编码 | varchar | 80 |  | √ | ' ' | 上级编码 |
| 17 | fcodetableversion | 编码表版本号 | varchar | 100 |  | √ | ' ' | 编码表版本号 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 20 | fexcisepolicy | 消费税政策依据 | varchar | 300 |  | √ | ' ' | 消费税政策依据 |
| 21 | fparentid | 上级 | int8 | 64 |  | √ | 0 | 税收分类编码 er_taxclasscode |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | ffullname | 长名称 | varchar | 100 |  | √ | ' ' | 长名称 |
| 24 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 25 | fdescription | 说明 | varchar | 2000 |  | √ | ' ' | 说明 |
| 26 | fvatspecialmanagement | 增值税特殊管理 | varchar | 400 |  | √ | ' ' | 增值税特殊管理 |
| 27 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 28 | fsimplename | 简称 | varchar | 100 |  | √ | ' ' | 简称 |
| 29 | fexcisespecialcontentnum | 消费税特殊内容代码 | varchar | 100 |  | √ | ' ' | 消费税特殊内容代码 |
| 30 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 32 | fmergecode | 合并编码 | varchar | 80 |  | √ | ' ' | 合并编码 |
| 33 | fvatspecialcontent | 增值税政策依据 | varchar | 255 |  | √ | ' ' | 增值税政策依据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_taxclasscode_pkey |  | fid |
| 2 | idx_er_taxclasscode_fnumber |  | fnumber |

---

## 税收分类编码-多语言表 t_er_taxclasscode_l

- **表名称：** 税收分类编码-多语言表
- **表名：** t_er_taxclasscode_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 4 | fsimplename | 简称 | varchar | 100 |  | √ | ' ' | 简称 |
| 5 | fkey | 关键字 | varchar | 2000 |  | √ | ' ' | 关键字 |
| 6 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 7 | fdescription | 说明 | varchar | 2000 |  | √ | ' ' | 说明 |
| 8 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_taxclasscode_l_pkey |  | fpkid |
| 2 | idx_er_tccode_l_fsimname |  | fsimplename |
| 3 | idx_er_tccode_l_fid_flcid |  | fid,flocaleid |
