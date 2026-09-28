# 资金账户-ocdbd_incentiveaccount

## 指定组织-多选基础资料表 t_ocdbd_ictaccorgs

- **表名称：** 指定组织-多选基础资料表
- **表名：** t_ocdbd_ictaccorgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_ictaccorgs |  | fpkid |
| 2 | idx_ocdbd_ictaccorgs_fbid |  | fbasedataid |

---

## 资金账户-主表 t_ocdbd_ictaccount

- **表名称：** 资金账户-主表
- **表名：** t_ocdbd_ictaccount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fisrebate | 计返利 | bpchar | 1 |  | √ | '0' | 计返利 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fissale | 计销量 | bpchar | 1 |  | √ | '0' | 计销量 |
| 8 | forguserange | 组织使用范围 | bpchar | 1 |  | √ | 'A' | 组织使用范围,枚举: A :全部组织 B :指定组织 |
| 9 | faccountclass | 账户类别 | bpchar | 1 |  | √ | 'A' | 账户类别,枚举: A :金额账户 B :数量金额账户 |
| 10 | fissupportitem | 支持商品明细账 | bpchar | 1 |  | √ | '0' | 支持商品明细账 |
| 11 | fiswinteracct | 是否冬储账户 | bpchar | 1 |  | √ | '0' | 是否冬储账户 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fisbudget | 计预算 | bpchar | 1 |  | √ | '0' | 计预算 |
| 17 | faccounttype | 账户标识 | bpchar | 1 |  | √ | ' ' | 账户标识,枚举: A :激励 B :费用 C :资金 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 20 | fissyspreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 21 | fismobileshow | 是否移动端展示 | bpchar | 1 |  | √ | '0' | 是否移动端展示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_ictaccount |  | fid |
| 2 | idx_ocdbd_ictaccount_num |  | fnumber |

---

## 资金账户-多语言表 t_ocdbd_ictaccount_l

- **表名称：** 资金账户-多语言表
- **表名：** t_ocdbd_ictaccount_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_ictaccountl_flid |  | fid,flocaleid |
| 2 | pk_ocdbd_ictaccount_l |  | fpkid |
