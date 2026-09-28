# 资产负债表-fsa_rptbalance

## 资产负债表-主表 t_fsa_rptbalance

- **表名称：** 资产负债表-主表
- **表名：** t_fsa_rptbalance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmappingsrctype | 映射来源 | bpchar | 1 |  | √ | ' ' | 映射来源,枚举: 0 :总账 1 :合并报表 9 :模拟数据 |
| 3 | fsrcitemid | 报表项目 | int8 | 64 |  | √ | 0 | 标准报表项目 fsa_rptitems |
| 4 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 5 | fendvalue | 期末值 | numeric | 23 | 2 | √ | 0 | 期末值 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fdel | 用于标记删除的Token信息 | int8 | 64 |  | √ | 0 | 用于标记删除的Token信息 |
| 8 | fbeginvalue | 期初值 | numeric | 23 | 2 | √ | 0 | 期初值 |
| 9 | facctbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 bd_accountbookstype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_rptbalance |  | fid |
| 2 | idx_fsa_rptbalance_2 |  | fsrcitemid,fdel |
| 3 | idx_fsa_rptbalance_1 |  | forgid,fperiodid,fdel |
