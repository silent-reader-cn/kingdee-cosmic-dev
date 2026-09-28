# 实物卡片版本-fa_card_version

## 实物卡片版本-主表 t_fa_card_version

- **表名称：** 实物卡片版本-主表
- **表名：** t_fa_card_version

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmasterid | 主数据ID | int8 | 64 |  | √ | 0 | 主数据ID |
| 3 | fbizperiodid | 发生期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 4 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fnumber | 资产编码 | varchar | 80 |  | √ | ' ' | 资产编码 |
| 6 | frealcardid | 实物信息 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 7 | fdepreuseid | 折旧用途 | int8 | 64 |  | √ | 0 | 折旧用途 fa_depreuse |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_version_frealcardid |  | frealcardid |
| 2 | idx_fa_version_num |  | fnumber |
| 3 | idx_fa_orguseperiod_master |  | forgid,fdepreuseid,fmasterid,fbizperiodid |
| 4 | pk_t_fa_card_version |  | fid |
| 5 | idx_fa_orguse_master |  | fmasterid,forgid |
