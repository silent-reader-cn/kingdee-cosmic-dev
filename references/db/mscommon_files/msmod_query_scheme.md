# 查询方案后台数据表-msmod_query_scheme

## 查询方案后台数据表-多语言表 t_msmod_query_scheme_l

- **表名称：** 查询方案后台数据表-多语言表
- **表名：** t_msmod_query_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msmod_query_scheme_l_fid |  | fid,flocaleid |
| 2 | pk_t_msmod_query_scheme_l |  | fpkid |

---

## 查询方案后台数据表-主表 t_msmod_query_scheme

- **表名称：** 查询方案后台数据表-主表
- **表名：** t_msmod_query_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fschemestr | 方案详情 | varchar | 255 |  | √ | ' ' | 方案详情 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fenable | 使用状态 | varchar | 50 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fschemestr_tag | 方案详情_详情 | text | 0 |  |  | null | 方案详情_详情 |
| 13 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 14 | fformid | 业务对象 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 15 | fisdefault | 是否默认方案 | bpchar | 1 |  | √ | '0' | 是否默认方案 |
| 16 | fwfpagekey | 核销页面标识 | varchar | 50 |  | √ | ' ' | 核销页面标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_msmod_query_scheme_fnumber |  | fnumber |
| 2 | pk_t_msmod_query_scheme |  | fid |
