# 信用档案-task_creditfiles

## 信用档案-多语言表 t_tk_creditfiles_l

- **表名称：** 信用档案-多语言表
- **表名：** t_tk_creditfiles_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fcorrectdescription | 修改说明 | varchar | 255 |  |  | ' ' | 修改说明 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_creditfiles_l_pkey |  | fpkid |
| 2 | t_tk_creditfiles_l_index |  | fid,flocaleid |

---

## 信用档案-主表 t_tk_creditfiles

- **表名称：** 信用档案-主表
- **表名：** t_tk_creditfiles

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 共享中心（废弃勿删） | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreditlevel | 信用等级 | int8 | 64 |  | √ | 0 | 信用等级 task_creditlevel |
| 5 | forgfield | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fuser | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 9 | fbonuspointnum | 加分次数 | int4 | 32 |  | √ | 0 | 加分次数 |
| 10 | forg | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fthisyearunqualifiednum | fthisyearunqualifiednum | int8 | 64 |  | √ | 0 |  |
| 13 | fctrlstrategy | fctrlstrategy | varchar | 30 |  | √ | ' ' |  |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 18 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fusernumber | 用户账号 | varchar | 50 |  | √ | ' ' | 用户账号 |
| 21 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 22 | fcreditvalue | 信用分数 | numeric | 23 | 1 | √ | 0.0 | 信用分数 |
| 23 | funqualifiedtotalnum | 扣分次数 | int8 | 64 |  | √ | 0 | 扣分次数 |
| 24 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tk_creditfiles_createorg |  | fcreateorgid |
| 2 | index_tk_creditfiles_org |  | forg |
| 3 | t_tk_creditfiles_pkey |  | fid |
| 4 | index_creditfiles_fcretorgid |  | fcreateorgid |
| 5 | index_tk_crefiles_modtime |  | fmodifytime |
| 6 | index_tk_creditfiles_orgfield |  | forgfield |
| 7 | idx_t_tk_creditfiles_master |  | fmasterid |
| 8 | index_tk_creditfiles_fuser |  | fuser |
