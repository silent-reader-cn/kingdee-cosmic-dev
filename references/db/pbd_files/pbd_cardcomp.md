# 卡片组件-pbd_cardcomp

## 卡片组件-多语言表 t_pbd_cardcomp_l

- **表名称：** 卡片组件-多语言表
- **表名：** t_pbd_cardcomp_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_cardcomp_l_fid |  | fid,flocaleid |
| 2 | pk_pbd_cardcomp_l |  | fpkid |

---

## 卡片组件-主表 t_pbd_cardcomp

- **表名称：** 卡片组件-主表
- **表名：** t_pbd_cardcomp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fdatasort_tag | 数据排序_详情 | varchar | 1000 |  | √ | ' ' | 数据排序_详情 |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [卡片组件分组 pbd_cardcomp_group](../pbd_files/pbd_cardcomp_group.md) |
| 7 | flimit | 数量限制 | int4 | 32 |  | √ | 0 | 数量限制 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fcheckitemid | 检查项 | int8 | 64 |  | √ | 0 | [检查项 pbd_check_item](../pbd_files/pbd_check_item.md) |
| 10 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcardoptionbindvalue | 配置值 | varchar | 255 |  | √ | ' ' | 配置值 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 18 | fcardtplid | 卡片模板 | int8 | 64 |  | √ | 0 | [卡片模板 pbd_cardtpl](../pbd_files/pbd_cardtpl.md) |
| 19 | fdatasort | 数据排序 | varchar | 255 |  | √ | ' ' | 数据排序 |
| 20 | fcardoptionbindvalue_tag | 配置值_详情 | text | 0 |  |  | null | 配置值_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_cardcomp |  | fid |
| 2 | idx_pbd_cardcomp_fnum |  | fnumber |
| 3 | idx_pbd_cardcomp_fgroupid |  | fgroupid |
