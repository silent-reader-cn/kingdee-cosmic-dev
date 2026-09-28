# 差旅项目-er_tripexpenseitem

## 差旅项目-多语言表 t_er_tripexpenseitem_l

- **表名称：** 差旅项目-多语言表
- **表名：** t_er_tripexpenseitem_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 252 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_tripexpenseitem_l_pkey |  | fpkid |
| 2 | idx_er_tpexpitem_l_flcid |  | fid,flocaleid |

---

## 差旅项目-使用范围位图表 t_er_tripexpenseitem_m

- **表名称：** 差旅项目-使用范围位图表
- **表名：** t_er_tripexpenseitem_m

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
| 1 | pk_t_er_tripexpenseitem_m |  | forgid |

---

## 差旅项目-使用范围表 t_er_tripexpenseitem_u

- **表名称：** 差旅项目-使用范围表
- **表名：** t_er_tripexpenseitem_u

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
| 1 | idx_t_er_tripexpenseitem_u_uo |  | fuseorgid |
| 2 | t_er_tripexpenseitem_u_pkey |  | fdataid,fuseorgid |

---

## 差旅项目-主表 t_er_tripexpenseitem

- **表名称：** 差旅项目-主表
- **表名：** t_er_tripexpenseitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 3 | fnoinvoice | 无票 | bpchar | 1 |  | √ | '0' | 无票 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fisvactax | 价税分离 | bpchar | 1 |  | √ | ' ' | 价税分离 |
| 7 | fisinit | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设,枚举: 1 :是 0 :否 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | foperationtype | 服务类型 | varchar | 30 |  | √ | ' ' | 服务类型,枚举: 1 :国内酒店 2 :国内机票 3 :国内用车 4 :国际机票 5 :国际酒店 6 :火车预订 7 :服务费 8 :用餐预订 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fexpenseitemiconmob | 移动端差旅明细图标 | varchar | 255 |  | √ | ' ' | 移动端差旅明细图标 |
| 15 | fctrltype | 控制类型 | varchar | 10 |  | √ | ' ' | 控制类型,枚举: 1 :定额 2 :实报实销（不填充金额） 3 :实报实销（自动填充金额） |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fisoffset | 可抵扣 | bpchar | 1 |  | √ | ' ' | 可抵扣 |
| 19 | fremark | 备注 | varchar | 252 |  | √ | ' ' | 备注 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 22 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | flongnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 25 | fmigsrc | fmigsrc | int4 | 32 |  | √ | 0 |  |
| 26 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 27 | fexpenseitemicon | 选择图标 | varchar | 255 |  | √ | ' ' | 选择图标 |
| 28 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | 短编码 | varchar | 30 |  | √ | ' ' | 短编码 |
| 30 | fattribute | 属性 | varchar | 30 |  |  | ' ' | 属性,枚举: 0 :空 1 :补助 2 :飞机 3 :汽车 4 :火车 5 :住宿 7 :轮船 8 :私车公用 9 :交通补贴 10 :伙食补贴 6 :其他 |
| 31 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 32 | fisdefault | 新增单据时显示 | bpchar | 1 |  | √ | ' ' | 新增单据时显示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_tripexpenseitem_pkey |  | fid |
| 2 | idx_t_er_tripexpenseitem_createorg |  | fcreateorgid |
| 3 | idx_er_tripexpenseitem_fenable |  | fenable |
| 4 | idx_t_er_tripexpenseitem_master |  | fmasterid |
| 5 | idx_er_tripexpenseitem_flnum |  | flongnumber |
