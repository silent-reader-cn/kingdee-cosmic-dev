# 序列号关联扩展配置-sbs_snrelextconfig

## 序列号关联扩展配置-主表 t_sbs_snrelextconfig

- **表名称：** 序列号关联扩展配置-主表
- **表名：** t_sbs_snrelextconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fdesttable | 映射目标 | varchar | 50 |  | √ | 'bd_snmainfile' | 映射目标,枚举: bd_snmainfile :序列号主档 bd_snmovetrack_rel :序列号轨迹关联表 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fdestcol | 目标表字段 | varchar | 50 |  | √ | ' ' | 目标表字段 |
| 7 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | finvflu | 库存更新方向 | varchar | 50 |  | √ | ' ' | 库存更新方向,枚举: 1 :库存增加 2 :库存减少 3 :库存转移 |
| 9 | fbillsncol | 单据序列号关联表字段 | varchar | 50 |  | √ | ' ' | 单据序列号关联表字段 |
| 10 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 11 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sbs_snrelextconfig_fbill |  | fbillsncol |
| 2 | idx_sbs_snrelextconfig_fdest |  | fdesttable,fdestcol |
| 3 | pk_t_sbs_snrelextconfig |  | fid |
