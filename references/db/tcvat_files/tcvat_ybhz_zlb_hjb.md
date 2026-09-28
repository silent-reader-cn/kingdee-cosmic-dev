# 一般汇总总览表合计表-tcvat_ybhz_zlb_hjb

## 一般汇总总览表合计表-主表 t_tcvat_ybhz_zlb_hjb

- **表名称：** 一般汇总总览表合计表-主表
- **表名：** t_tcvat_ybhz_zlb_hjb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjzsehj | 减征税额合计 | numeric | 23 | 10 | √ | 0 | 减征税额合计 |
| 3 | fybtsehj | 应补退税额合计 | numeric | 23 | 10 | √ | 0 | 应补退税额合计 |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fybhwjlwsehjjzjt | 一般货物及劳务即征即退税额合计 | numeric | 23 | 10 | √ | 0 | 一般货物及劳务即征即退税额合计 |
| 6 | fysfwsehjjzjt | 应税服务即征即退税额合计 | numeric | 23 | 10 | √ | 0 | 应税服务即征即退税额合计 |
| 7 | ffpxssrhj | 分配销售收入合计 | numeric | 23 | 10 | √ | 0 | 分配销售收入合计 |
| 8 | fjxsjdksehj | 进项实际抵扣税额合计 | numeric | 23 | 10 | √ | 0 | 进项实际抵扣税额合计 |
| 9 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 10 | fyjsjhj | 预缴税金合计 | numeric | 23 | 10 | √ | 0 | 预缴税金合计 |
| 11 | fybhwjlwsehj | 一般货物及劳务税额合计 | numeric | 23 | 10 | √ | 0 | 一般货物及劳务税额合计 |
| 12 | fysfwsehj | 应税服务税额合计 | numeric | 23 | 10 | √ | 0 | 应税服务税额合计 |
| 13 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_ybhz_zlb_hjb |  | fid |
| 2 | idx_tcvat_ybhz_zlb_hjb |  | forgid,fstartdate,fenddate |
