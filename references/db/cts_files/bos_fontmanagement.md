# 管理打印字体-bos_fontmanagement

## 管理打印字体-主表 t_bas_fontmanagement

- **表名称：** 管理打印字体-主表
- **表名：** t_bas_fontmanagement

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapprovedate | fapprovedate | timestamp | 0 |  |  | null |  |
| 3 | fapproverid | fapproverid | int8 | 64 |  | √ | 0 |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | fisv | 开发商标识 | varchar | 8 |  | √ | ' ' | 开发商标识 |
| 7 | fforbidstatus | fforbidstatus | bpchar | 1 |  | √ | ' ' |  |
| 8 | ftenantid | 租户ID | varchar | 80 |  | √ | ' ' | 租户ID |
| 9 | fsource | 来源 | bpchar | 1 |  | √ | '1' | 来源,枚举: 1 :系统预置 2 :自定义 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fforbiderid | fforbiderid | int8 | 64 |  | √ | 0 |  |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 17 | ffontname | 字体名称 | varchar | 80 |  | √ | ' ' | 字体名称 |
| 18 | fforbiddate | fforbiddate | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_fontmanagement_pkey |  | fid |
| 2 | idx_bas_fontmanagement |  | fnumber |

---

## 管理打印字体-多语言表 t_bas_fontmanagement_l

- **表名称：** 管理打印字体-多语言表
- **表名：** t_bas_fontmanagement_l

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
| 1 | t_bas_fontmanagement_l_pkey |  | fpkid |
| 2 | idx_bas_fontmanagement_l |  | fid,flocaleid |
