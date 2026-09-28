# 工艺路线成本计算临时存储表-cad_calprocessroutecost

## 工艺路线成本计算临时存储表-主表 t_cad_calprocessroutecost

- **表名称：** 工艺路线成本计算临时存储表-主表
- **表名：** t_cad_calprocessroutecost

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty | 耗用量 | numeric | 23 | 10 | √ | 0.0000000000 | 耗用量 |
| 3 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 4 | fcosttypeid | 成本类型 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fresourceid | 资源 | int8 | 64 |  | √ | 0 | [资源维护(废弃) mpdm_resources](../mpdm_files/mpdm_resources.md) |
| 7 | factivityid | 工序活动 | int8 | 64 |  | √ | 0 | [工序活动定义(废弃) mpdm_processactivity](../mpdm_files/mpdm_processactivity.md) |
| 8 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 9 | fcalcbasis | 计算依据 | varchar | 30 |  | √ | ' ' | 计算依据,枚举: 001 :资源工时 002 :物料 003 :批次 |
| 10 | frouterid | 成本工艺路线 | int8 | 64 |  | √ | 0 | [分组基础资料带组织模板 cad_router](../basedata_files/cad_router.md) |
| 11 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 12 | fcost | 成本 | numeric | 23 | 10 | √ | 0.0000000000 | 成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cad_calprocessroutecost |  | fcosttypeid,frouterid |
| 2 | pk_t_cad_calprocessroutecost |  | fid |
