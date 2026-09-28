# 动态算法卡片-fa_card_dynamic

## 动态算法卡片-主表 t_fa_card_dynamic

- **表名称：** 动态算法卡片-主表
- **表名：** t_fa_card_dynamic

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentityname | 切换动态算法的单据实体编码 | varchar | 30 |  | √ | ' ' | 切换动态算法的单据实体编码 |
| 3 | fperiodid | fperiodid | int8 | 64 |  | √ | 0 |  |
| 4 | fchangebillid | 切换动态算法的单据id | int8 | 64 |  | √ | 0 | 切换动态算法的单据id |
| 5 | fdate | 切换日期 | timestamp | 0 |  |  | null | 切换日期 |
| 6 | frealcardid | 实物卡片 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 7 | fassetbookid | 资产账簿 | int8 | 64 |  | √ | 0 | 启用期间设置 fa_assetbook |
| 8 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | 会计政策 xkbd_policy |
| 9 | fdepreuseid | 折旧用途 | int8 | 64 |  | √ | 0 | 折旧用途 fa_depreuse |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_card_dynamic_pkey |  | fid |
| 2 | idx_fa_dyncard_c |  | frealcardid,fassetbookid,fdepreuseid |
| 3 | idx_fa_dyncard_b |  | fentityname,fchangebillid |
| 4 | idx_fa_dyncard_p |  | fassetbookid,fperiodid |
