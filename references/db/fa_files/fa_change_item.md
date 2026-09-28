# 变更项目-fa_change_item

## 变更项目-主表 t_fa_change_item

- **表名称：** 变更项目-主表
- **表名：** t_fa_change_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fischange | 新增当期允许变更 | bpchar | 1 |  | √ | '0' | 新增当期允许变更 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ftopic | 来源类型 | varchar | 30 |  | √ | ' ' | 来源类型,枚举: fa_card_real :资产卡片实物信息 fa_card_fin :资产卡片财务信息 fa_lease_contract :租赁合同 |
| 7 | fisgenvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fpreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 13 | fbackfield | 初始字段 | varchar | 30 |  | √ | ' ' | 初始字段,枚举: |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编号 | varchar | 100 |  | √ | ' ' | 编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_change_item |  | fnumber |
| 2 | t_fa_change_item_pkey |  | fid |

---

## 变更项目-多语言表 t_fa_change_item_l

- **表名称：** 变更项目-多语言表
- **表名：** t_fa_change_item_l

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
| 1 | idx_fa_change_item_l |  | fid,flocaleid |
| 2 | t_fa_change_item_l_pkey |  | fpkid |
