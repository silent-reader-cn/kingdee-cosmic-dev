# 证监会行业-csrc_industry_info

## 证监会行业-多语言表 t_csrc_industry_info_l

- **表名称：** 证监会行业-多语言表
- **表名：** t_csrc_industry_info_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 行业名称 | varchar | 50 |  | √ | ' ' | 行业名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_csrc_industry_info_l |  | fpkid |
| 2 | idx_csrc_industry_info_l_0 |  | fid,flocaleid |

---

## 证监会行业-主表 t_csrc_industry_info

- **表名称：** 证监会行业-主表
- **表名：** t_csrc_industry_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 说明 | varchar | 500 |  | √ | ' ' | 说明 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | findustrylevel | 行业层级 | varchar | 50 |  | √ | ' ' | 行业层级 |
| 4 | fname | 行业名称 | varchar | 50 |  | √ | ' ' | 行业名称 |
| 5 | fcyb_industry | 创业板行业属性 | varchar | 50 |  | √ | ' ' | 创业板行业属性,枚举: GL :鼓励行业 XZ :限制行业 JZ :禁止行业 CNGS :产能过程行业 TT :《产业结构调整指导目录》中的淘汰类行业 |
| 6 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 证监会行业分类 csrc_industry_type |
| 8 | fshowrows | 显示顺序 | int4 | 32 |  | √ | 0 | 显示顺序 |
| 9 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fkcb_industry | 科创板行业属性 | varchar | 50 |  | √ | ' ' | 科创板行业属性,枚举: GL :鼓励行业 XZ :限制行业 JZ :禁止行业 CNGS :产能过程行业 TT :《产业结构调整指导目录》中的淘汰类行业 |
| 11 | fbjs_industry | 北交所行业属性 | varchar | 50 |  | √ | ' ' | 北交所行业属性,枚举: GL :鼓励行业 XZ :限制行业 JZ :禁止行业 CNGS :产能过程行业 TT :《产业结构调整指导目录》中的淘汰类行业 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 行业编码 | varchar | 30 |  | √ | ' ' | 行业编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_csrc_industry_info |  | fid |
| 2 | uk_csrc_industry_info_number |  | fnumber |
